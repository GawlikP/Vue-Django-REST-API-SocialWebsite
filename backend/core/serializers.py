from rest_framework import serializers

from .models import Account 
from rest_framework.authtoken.models import Token

class ResterSerialier(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account 
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
            
        }

    def save(self):
        
        acc = Account ( 
            email= self.validated_data['email'],
            username= self.validated_data['username']
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error':'Passwords must match!'})
        acc.set_password(password)
        acc.save()
        return acc

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



    def log_me_in(self):
        accs =  Account.objects.filter(username= self.validated_data['username'])
        if accs.count() > 0:
            acc = Account.objects.get(username= self.validated_data['username'])
            if acc.check_password(self.validated_data['password']):
                return acc
            else:
                raise serializers.ValidationError({'error' : 'Wrong password!'})
        else:
            raise serializers.ValidationError({'error': 'User does not exits!'})

class AuthTokenSerializer(serializers.Serializer):

    token = serializers.CharField()

    def check_token(self):
        if Token.objects.filter(key=self.validated_data['token']).exists():
            token = Token.objects.get(key=self.validated_data['token'])
            return True
            
        else:
            raise serializers.ValidationError({'error': 'Token does not exist!'})
        
        return False

class AccountSerializer(serializers.ModelSerializer):

     class Meta:
        model = Account 
        fields = ['id','email', 'username', 'password', 'created']
        extra_kwargs = {
            'password': {'write_only': True}
        }