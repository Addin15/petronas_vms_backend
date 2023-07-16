from knox.crypto import hash_token
from django.utils import timezone
from datetime import datetime
from rest_framework import authentication
from rest_framework import exceptions

from knox.models import AuthToken

from  .models import User

class CustomTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return None

        try:
            # Get token
            token = token.split(" ")[1]

            user_token = AuthToken.objects.get(digest=hash_token(token=token))
            id = user_token.user_id
            user = User.objects.filter(id=id).first()
            user.last_login = datetime.now(tz=timezone.utc)
            user.save()
        except Exception as e:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)