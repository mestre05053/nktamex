# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from users.serializers import RegisterSerializer
from rest_framework import status

'''
user mestre05053
pass Lambada1986_Samoa
email mestre05053@lambada.com
token 602ac6ab4f67760cccbeb912c4f34e12afc9cca1494225b59690a6dfc654d9fb
'''

def serialize_user(user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })
        

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })


@api_view(['GET'])
def get_user(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_data': serialize_user(user)
        })
    return Response({'error':'No estas logueado, no tienes acceso sin logearte'}, status.HTTP_400_BAD_REQUEST)