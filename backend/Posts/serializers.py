from rest_framework import serializers
from Posts.models import Post




class PostSerializer(serializers.Serializer):
    
   # created = serializers.DateTimeField()
    id = serializers.IntegerField(read_only=True)
    deleted = serializers.BooleanField(default=False)
    title = serializers.CharField(max_length=512, default='error')
    content = serializers.CharField(default= '')
    hearts = serializers.IntegerField()

    def create(self, validated_data):

        return Post.objects.create(**validated_data)

    


    
