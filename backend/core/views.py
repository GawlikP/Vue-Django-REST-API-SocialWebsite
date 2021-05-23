from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import decorators

# Create your views here.

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.serializers import Serializer
from .models import Account

from .serializers import ResterSerialier, LoginSerializer, AuthTokenSerializer, AccountSerializer

from hearts.models import Heart
from hearts.serializers import HeartSerializer

from profiles.models import Profile
from profiles.serializers import ProfileSerializer

from commentslikes.models import CommentLike
from commentslikes.serializers import CommentLikeSerializer

from follows.models import Follow
from follows.serializers import FollowSerializer

from posts.models import Post
from posts.serializers import PostSerializer

from profiles.models import Profile

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def accounts_list(request, fromat=None):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


    if request.method == 'POST':
        serialzier = ResterSerialier(data= request.data)
        data = {}
        if serialzier.is_valid():
            account = serialzier.save()
            profile = Profile(note="", description="", account=account)
            profile.save()
            data = serialzier.data
            token = Token.objects.get(user=account)
            data['token'] = token.key
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serialzier.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
@api_view(['GET'])
@permission_classes([AllowAny])
def account_defails(request, pk, format=None):
    

        try:
            acc = Account.objects.get(pk= pk)
        except Account.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = AccountSerializer(acc)
            return JsonResponse(serializer.data)



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
    user = request.user
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_hearts(request, format=None):
    if request.method == 'GET':
        account = request.user.id
        hearts = Heart.objects.filter(account= account)
        if hearts.exists():
            serializer = HeartSerializer(hearts, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
        data = {}
        data['error'] = 'No hearts to return'
        return JsonResponse(data= data, status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_profile(request, format=None):
    acc =request.user
    try:
        profile = Profile.objects.get(account= acc)
    except Profile.DoesNotExist:
        data = {}
        data['error'] = 'Profile does not exists'
        return JsonResponse(data=data,status=status.HTTP_404_NOT_FOUND)  
        
    serializer = ProfileSerializer(profile)
        
    return JsonResponse(data=serializer.data, status=status.HTTP_200_OK, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_commentslikes(request, format=None):
    if request.method == 'GET':
        account = request.user.id
        commentslikes = CommentLike.objects.filter(account= account)
        if commentslikes.exists():
            serializer = CommentLikeSerializer(data= commentslikes, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        data = {}
        data['error'] = 'No commentslikes to return'
        return JsonResponse(data= data, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_follows(request, format=None):
    if request.method == 'GET':
        account = request.user.id 
        follows = Follow.objects.filter(following= account)
        if follows.exists():
            serializer = FollowSerializer(data= follows, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        data = {}
        data['error'] = 'No follows to return'
        return JsonResponse(data=data, status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_followers(request, format=None):
    if request.method == 'GET':
        account = request.user.id
        following = Follow.objects.filter(follower= account)
        if following.exists():
            serializier = FollowSerializer(data= following,many= True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        data = {}
        data['error'] = 'No follows to return'
        return JsonResponse(data=data, status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_id_posts(request,pk, format=None):
    try:
        acc = Account.objects.get(pk= pk)
    except Account.DoesNotExist:
        data = {}
        data['error'] = 'Account does not exists'
        return JsonResponse(data=data,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        posts = Post.objects.filter(author= acc)
        if posts.exists():
            serialzier = PostSerializer(data=posts, many=True)
            return JsonResponse(serialzier.data, status=status.HTTP_200_OK)
        data = {}
        data['error'] = 'No posts to return'
        return JsonResponse(data=data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_posts(request, format=None):
    if request.method == 'GET':
        account = request.user.id
        posts = Post.objects.filter(author= account)
        if posts.exists():
            serializer = PostSerializer(data=posts, many=True)
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        data = {}
        data['error'] = 'No posts to return'
        return JsonResponse(data=data, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_id_profile(request, pk, format=None):

    try:
        acc = Account.objects.get(pk= pk)
    except Account.DoesNotExist:
        data = {}
        data['error'] = 'Account does not exists'
        return JsonResponse(data=data,status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        
        try:
            profile = Profile.objects.get(account= acc)
        except Profile.DoesNotExist:
            data = {}
            data['error'] = 'Profile does not exists'
            return JsonResponse(data=data,status=status.HTTP_404_NOT_FOUND)  
        
        serializer = ProfileSerializer(profile)
        
        return JsonResponse(data=serializer.data, status=status.HTTP_200_OK)
   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_account(request, format=None):
    

        try:
            acc = Account.objects.get(pk= request.user.id)
        except Account.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = AccountSerializer(acc)
            return JsonResponse(serializer.data)



        



