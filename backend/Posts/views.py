from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

from Posts.serializers import PostSerializer
from Posts.models import Post
from rest_framework import status 



# endpoint dla pobierania i tworzenia postow


@api_view(['GET', 'POST'])
def post_list(request, format=None):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == 'POST':
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serailzer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
# endpoint dla modyfikacji i detali postow 

@api_view(['GET', 'PUT'])
def post_detail(request, pk, format=None):

    # pk = PRIMARY KEY

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #endpoint sluzacy do oddawania szczegolow na temat jednego poszczegolnego posta

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)

    # za kazdym razem jak edytujemy jakiekolwiek wartosci naszego posta, uzywamy tego endpoita

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PostSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    



