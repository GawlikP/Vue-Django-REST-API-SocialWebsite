from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions, serializers
from rest_framework.settings import perform_import
from rest_framework.urlpatterns import format_suffix_patterns

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import JSONParser

from .serializers import CommentLikeSerializer
from .models import CommentLike
from rest_framework import status 

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def commentslikes_list(request, format=None):
    if request.mothod == 'GET':
        commentslikes = CommentLike.objects.all()
        serializer = CommentLikeSerializer(commentslikes, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        data['account'] = request.user.id

        serializer = CommentLikeSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def commentslike_detail(request, pk, format=None):
    try:
        commentslike = CommentLike.objects.get(pk=pk)
    except CommentLike.DoesNotExist:
        data['error'] = 'CommentLike does not exist'
        return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CommentLikeSerializer(commentslike)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentLikeSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
>>>>>>> ab96b025ec016009b48760b46ca03cd2404e4212
