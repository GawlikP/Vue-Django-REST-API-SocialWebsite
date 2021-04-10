

from rest_framework import serializers 

from .models import Heart

from core.models import Account
from Posts.models import Post


class HeartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Heart
        fields = ['id', 'created', 'post', 'account']

