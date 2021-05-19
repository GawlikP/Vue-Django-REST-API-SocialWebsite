from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    
    description = serializers.CharField(allow_blank=True)
    note = serializers.CharField(allow_blank=True)
    class Meta:
        model = Profile
        fields = ['id', 'created', 'description', 'note', 'account']
