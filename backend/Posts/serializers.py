from rest_framework import serializers
from Posts.models import Post




class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'created', 'deleted', 'title', 'content', 'hearts']
   

    


    
