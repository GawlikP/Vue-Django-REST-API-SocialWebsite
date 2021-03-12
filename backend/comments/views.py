from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

#? Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser

from comments.serializers import CommentSerializer
from comments.models import Comment
from rest_framework import status 
# Create your views here.

#? endpoint dla pobierania i tworzenia komentarzy

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comments_list(request, format=None):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == 'POST':
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET', 'PUT'])
@permission_classes([AllowAny])
def comments_detail(request, pk, format=None):
    
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
     #? endpoint sluzacy do oddawania szczegolow na temat jednego poszczegolnego KOMENTARZA

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data)
        
    #? za kazdym razem jak edytujemy jakiekolwiek wartosci naszego komentarza, uzywamy tego endpoita

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)   
        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
