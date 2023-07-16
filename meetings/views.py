from datetime import datetime
import io
from tkinter import Image
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from rest_framework.decorators import APIView, api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from meetings.emails import confirmed_email, send_invitation
from users.authentication import CustomTokenAuthentication
from .models import Meeting, Invitation
from .serializers import InvitationSerializer, MeetingSerializer
from users.views import SCOPES
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from qrcode import make, QRCode
import pytz

# Create your views here.
class MeetingView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        user = request.user

        goauth = user.google_token

        if not goauth:
            return Response(data={'message': 'User is not authorized'}, status=status.HTTP_412_PRECONDITION_FAILED)

        creds = Credentials.from_authorized_user_info(goauth, SCOPES)

        serializer = MeetingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        meeting = Meeting.objects.create(
                summary=data['summary'],
                description=data['description'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                purpose=data['purpose'],
                venue=data['venue']
        )

        attendees = []

        calendar_service = build('calendar', 'v3', credentials=creds)
        email_service = build('gmail', 'v1', credentials=creds)
 
        for email in data['visitor_emails']:
            attendees.append({'email': email})
            invitation = Invitation.objects.create(
                host=request.user,
                meeting=meeting,
                visitor_email=email,
            )

            kuala_lumpur=pytz.timezone('Asia/Kuala_Lumpur')

            if invitation:

                # Create calendar meeting
                event = {
                    'summary': data['summary'],
                    'location': data['venue'],
                    'description': data['description'],
                    'start': {
                        'dateTime': data['start_date'].astimezone(kuala_lumpur).isoformat(), #'2015-05-28T09:00:00-07:00'
                        'timeZone': 'Asia/Kuala_Lumpur',
                    },
                    'end': {
                        'dateTime': data['end_date'].astimezone(kuala_lumpur).isoformat(),
                        'timeZone': 'Asia/Kuala_Lumpur',
                    },
                    # 'recurrence': [
                    #     'RRULE:FREQ=DAILY;COUNT=2'
                    # ],
                    'attendees':attendees,
                    'reminders': {
                        'useDefault': True,
                        # 'overrides': [
                        # {'method': 'email', 'minutes': 24 * 60},
                        # {'method': 'popup', 'minutes': 10},
                        # ],
                    },
                }

                event = calendar_service.events().insert(calendarId='primary', body=event).execute()

                # Send email the link for pre-reg

                create_message = send_invitation(email, request.user.email, invitation.id)


                send_message = (email_service.users().messages().send
                        (userId=request.user.email, body=create_message).execute())
                
                print(send_message)

        return Response(data=data, status=status.HTTP_201_CREATED);



    def get(self, request):
        
        meetings = Meeting.objects.all()

        serializer = InvitationSerializer(meetings, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK);


class InvitationView(APIView):
    authentication_classes = []

    def post(self, request, id):
        data = request.data

        if data.get('visitor_nric') == None:
            return Response(data={'message':'NRIC not provided'}, status=status.HTTP_400_BAD_REQUEST)

        # CAN CROSS CHECK THE NRIC HERE

        invitation = Invitation.objects.filter(id=id).first()
        invitation.visitor_nric = data['visitor_nric']
        invitation.is_preregistered = True
        invitation.save()

        goauth = invitation.host.google_token

        if not goauth:
            return Response(data={'message': 'User is not authorized'}, status=status.HTTP_412_PRECONDITION_FAILED)

        creds = Credentials.from_authorized_user_info(goauth, SCOPES)

        email_service = build('gmail', 'v1', credentials=creds)
        create_message = confirmed_email(invitation.visitor_email, invitation.host.email)
        send_message = (email_service.users().messages().send
                (userId=invitation.host.email, body=create_message).execute())
        
        print(send_message)

        serializer = InvitationSerializer(invitation)

        return Response(data={'status':'done', 'invitation': serializer.data}, status=status.HTTP_200_OK)


    def get(self, request, id):
        try:
            invitation = Invitation.objects.filter(id=id).first()
        except:
            return Response(data={'message':'Invitation ID invalid'}, status=status.HTTP_400_BAD_REQUEST)

        if not invitation:
            return Response(data={'message':'Invitation ID not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = InvitationSerializer(invitation)

        if invitation.is_preregistered:
            return Response(data={'status':'done', 'invitation': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(data={'status':'pending', 'invitation': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([])
def generate_qr(request, id):

    try:
        invitation = Invitation.objects.filter(id=id).first()
    except:
        return Response(data={'message':'Invitation ID invalid'}, status=status.HTTP_400_BAD_REQUEST)

    if not invitation:
        return Response(data={'message':'Invitation ID not found'}, status=status.HTTP_404_NOT_FOUND)
    
    qr = QRCode()
    qr.add_data(str(invitation.id)+str(invitation.meeting.id))

    im = qr.make_image()

    img_byte_arr = io.BytesIO()
    im.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return HttpResponse(img_byte_arr, content_type="image/png")