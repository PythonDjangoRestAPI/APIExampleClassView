from django.contrib.auth import authenticate
from requests import Response
from rest_framework import status

from api import messages
from api.models import User
from api.serializers import UserProfileSerializer


def check_user_exists_for_login(email):
    try:
        User.objects.get(email=email)
        return True
    except User.DoesNotExist:
        #logger.error("Login error: login request for non-existent user with email \"%s\"" % email)
        return Response(
            messages.USER_WITH_EMAIL_DOES_NOT_EXISTS,
            status=status.HTTP_404_NOT_FOUND)


def authenticate_user(email, password,request=None):
    user = User.objects.get(email=email)
    user = authenticate(email=email,password=password)
    if user:
        seralizer=UserProfileSerializer(user,data=request.DATA)
        seralizer_dict=seralizer.data
        seralizer_dict["message"]="Login Successful"
        return Response(seralizer_dict, status=status.HTTP_200_OK)
    else:
        return Response(
            messages.INVALID_EMAIL_OR_PASSWORD,
            status=status.HTTP_401_UNAUTHORIZED)