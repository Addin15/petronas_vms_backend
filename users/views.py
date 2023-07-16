import json
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from knox.models import AuthToken

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from . authentication import CustomTokenAuthentication
from . import serializers
from . models import User

SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://mail.google.com/']

@api_view(['POST'])
@authentication_classes([CustomTokenAuthentication])
@permission_classes([IsAuthenticated])
def google_authorize(request):
    user: User = request.user;
    creds = None

    goauth = user.google_token

    if goauth:
        creds = Credentials.from_authorized_user_info(goauth, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            try:
                creds = flow.run_local_server(port=5000,timeout_seconds=15)
            except:
                return Response(status=status.HTTP_412_PRECONDITION_FAILED)

        # Save the credentials for the next run
        user.google_token = json.loads(creds.to_json())
        user.save()

    goauth = user.google_token

    if goauth:
        return Response()
    else:
        return Response(status=status.HTTP_412_PRECONDITION_FAILED)
    


@api_view(['POST'])
@authentication_classes([])
def register(request):
    serializer = serializers.UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    user = User.objects.create(
        email=data['email'],
        name=data['name'],
        phone=data['phone'],
        password=make_password(data['password']),
    )

    if not user:
        return Response(data={'message':'Registration Failed'}, status=status.HTTP_400_BAD_REQUEST)

    token = AuthToken.objects.create(user=user)[1]

    user = serializers.UserSerializer(user)

    return Response(data={'user': user.data, 'token': token,}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([])
def login(request):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    user = User.objects.filter(email=data['email']).first()

    if not user:
        return Response(data={'message':'Email or password is invalid'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not user.check_password(data['password']):
        return Response(data={'message':'Email or password is invalid'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token = AuthToken.objects.create(user=user)[1]

    user = serializers.UserSerializer(user)

    return Response(data={'user': user.data, 'token': token,}, status=status.HTTP_201_CREATED)


