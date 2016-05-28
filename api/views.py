# Create your views here.
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import logging

from rest_framework.renderers import JSONRenderer

from api.serializers import UserProfileSerializer
from api.utils import check_user_exists_for_login, authenticate_user


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializers = UserProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    response_login={}
    try:
        email=request.data['email']
        password=request.data['password']
        user_type=request.data['user_type']
    except:
        return Response(
            {"message":"required field missing."},
            status=status.HTTP_400_BAD_REQUEST
        )
    response = check_user_exists_for_login(email)
    if response is True:
        return authenticate_user(email,password,request=request)
    else:
        return response