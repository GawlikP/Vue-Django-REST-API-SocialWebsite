from backend.follows.models import Follow
from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework import serializers
from rest_framework.serializers import Serializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser
# Create your views here.

from .models import Follow
from .serializers import FollowSerializer

class FollowViewSet(viewsets.ModelViewSet):

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = request.data
        data['account'] = request.user.id
        serialzier = serialzier_class(data= data)
        if serialzier.is_valid():
            serialzier.save()
            return JsonResponse(serialzier.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialzier.errors, status=status.status.HTTP_405_METHOD_NOT_ALLOWED)



