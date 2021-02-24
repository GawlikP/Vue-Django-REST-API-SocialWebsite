from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

from Accounts.serializers import RegisterSerializer, AccountSerializer, LoginSerializer
from Accounts.models import Account
from rest_framework import status 


@api_view(['POST', 'GET'])
def account_list(request, format=None):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET', 'PUT'])
def account_detail(request, pk, format=None):
    try: 
        acc = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AccountSerializer(acc)
        return JsonResponse(serializer.data)
        

@api_view(['POST'])
def account_login(request, format=None):
    if request.method == 'POST':
        data = {}
        serialzier = LoginSerializer(data=request.data)
        if serialzier.is_valid():
            acc = serialzier.login()
            data['login'] = serialzier.data['nick']
            data['token'] = acc.token
            data['blocked'] = acc.blocked
            data['moderator'] = acc.moderator
            return JsonResponse(data, status=status.HTTP_201_CREATED)

        return JsonResponse(serialzier.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
