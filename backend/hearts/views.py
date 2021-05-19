from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer

from rest_framework.viewsets import ModelViewSet

from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.parsers import JSONParser
# Create your views here.

from .models import Heart
from core.models import Account
from .serializers import HeartSerializer

class HeartViewSet(viewsets.ModelViewSet):

    queryset = Heart.objects.all()
    serializer_class = HeartSerializer
    permission_classes = [IsAuthenticated]  

    def create(self, request):
        data = request.data
        data['account'] = request.user.id
        accs = Heart.objects.filter(post=data['post'], account=data['account'])
        if accs.exists():
            data2 = {}
            data2['error'] = 'You cannot like the same post!'
            return JsonResponse(data=data2, status=status.HTTP_406_NOT_ACCEPTABLE)
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

 