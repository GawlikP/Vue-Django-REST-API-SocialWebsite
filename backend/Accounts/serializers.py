from rest_framework import serializers
from Accounts.models import Account

from datetime import datetime
from pprint import pprint


import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class AccountSerializer(serializers.ModelSerializer):
     class Meta:
        
        model = Account
        fields = ['id', 'created',
                'deleted','blocked',
                'moderator','nick',
                'last_login'
                ]
       

    

class RegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = Account
        fields = ['id', 'created',
                'deleted','blocked',
                'moderator','nick',
                'password','last_login',
                'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def save(self):
        account = Account(
            nick = self.validated_data['nick'],
            password = self.validated_data['password'],
            last_login = datetime.now()   
        )
        password  = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.password = password
        account.save()
        return account

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = ['id', 'created',
                'deleted','blocked',
                'moderator','nick', 'password',
                'last_login', 'token'
                ]
        extra_kwargs = {
           
            'nick': {'validators': []}
        }

    def login(self):

        check = Account.objects.filter(nick=self.validated_data['nick']).exists()
        if not check:
            raise serializers.ValidationError({'nick': 'Nick does not exist'})
            return
        acc = Account.objects.get(nick=self.validated_data['nick'])
        pprint(vars(acc))
        if not acc.password == self.validated_data['password']:
            raise serializers.ValidationError({'password': 'Password dont match'})
            return
        check = True
        token = ''
        while check:
            token = id_generator(128)
            check = Account.objects.filter(token=token)
            if check:
                token = id_generator(128)
        acc.token = token
        acc.last_login = datetime.now()
        acc.save()
        return acc
    