from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

from Posts.serializers import PostSerializer
from Posts.models import Post
from rest_framework import status 



@api_view(['GET'])
def post_list(request, format=None):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)