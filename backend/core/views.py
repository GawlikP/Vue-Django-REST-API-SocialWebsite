from django.shortcuts import render

# Create your views here.

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from .models import Account

from .serializers import ResterSerialier, LoginSerializer, AuthTokenSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def accounts_list(request, fromat=None):
    if request.method == 'POST':
        serialzier = ResterSerialier(data= request.data)
        data = {}
        if serialzier.is_valid():
            account = serialzier.save()
            data = serialzier.data
            token = Token.objects.get(user=account)
            data['token'] = token.key
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialzier.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
@api_view(['POST'])
@permission_classes([AllowAny])
def accounts_login(request, format=None):
    if request.method == 'POST':
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            account = serializer.log_me_in()
            data = serializer.data
            token = Token.objects.get(user= account)
            token.delete()
            token = Token.objects.create(user= account)
            data['token'] = token.key
            return JsonResponse(data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def auth_test_view(request):
    return JsonResponse({'response' : 'U HAVE PERMISSION!'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def check_token(request ):
    if request.method == 'POST':
        serializer = AuthTokenSerializer(data= request.data)
        if serializer.is_valid():
            success = serializer.check_token()
            if success:
                JsonResponse(serializer.data, status=status.HTTP_200_OK)
            else:
                JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
