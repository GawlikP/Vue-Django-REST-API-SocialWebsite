from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser

from rest_framework import  status

from .serializers import ProfileSerializer
from .models import Profile

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def profiles_list(request, format=None):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == 'POST':
        data = request.data 
        data['account'] = request.user.id 

        serializer = ProfileSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_detail(request, pk, format=None):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        data = {}
        data['error'] = 'Profile does not exist'
        return JsonResponse(json.dumps(data),status=status.HTTP_404_NOT_FOUND, safe=False)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        acc = request.user.id
        if profile.account.id != acc:
            data= {}
            data['error'] = 'It is not ur profile!'
            return JsonResponse(json.dumps(data), status=status.HTTP_401_UNAUTHORIZED, safe=False)
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


