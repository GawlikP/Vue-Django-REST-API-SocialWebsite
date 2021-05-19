from rest_framework import serializers
from .models import Post
from core.models import Account




class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'created', 'deleted', 'title', 'content', 'hearts', 'author']
   
class PostListSerializer(serializers.ModelSerializer):



    class Meta:
        model = Post
        fields = ['id', 'created', 'deleted', 'title', 'content', 'hearts', 'author', 'author']
        extra_kwargs = {
            'author': {'write_only' : True}
        }
  

    

    


    
