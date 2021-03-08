from django.test import TestCase
import json

# Create your tests here.


from rest_framework.authtoken.models import Token
from core.models import Account
from rest_framework.parsers import JSONParser

from rest_framework.test import APIClient

class AccountTestCase(TestCase):
    
    def setUp(self):
        Account.objects.create(username='test1', email='test1@gmail.com')
        Account.objects.create(username='test2', email='test2@gmail.com')

        self.client = APIClient()

        self.user_1 = Account.objects.get(username='test1')
        self.user_1.set_password('test1')
        self.user_1.save()
        self.user_2 = Account.objects.get(username='test2')
        self.user_2.set_password('test2')
        self.user_2.save()

        self.token_1 = Token.objects.get(user=self.user_1)
        self.token_2 = Token.objects.get(user=self.user_2)

    #! kazdy test musi zaczynac sie od 'test_'
    def test_did_new_users_get_tokens(self):
        user_3 = Account.objects.create(username='test', email='test@gmail.com')

        self.assertIsNotNone(Token.objects.get(user=user_3).key)
        self.assertIsNotNone(self.token_1.key)
        self.assertEqual(Account.objects.count(), 3)

    def test_auth_without_token(self):
        
        data = {}
        response = self.client.patch( 
        '/accounts/im_auth/',
        (data),
        content_type='application/json',
        **{'HTTP_X_BULK_OPERATION':'true'}
        )
        print(response.json())
        self.assertEqual(401, response.status_code)
    
    def test_can_sm_register(self):

        data = {
            "username": "test3", 
            "password": "test3",
            "password2": "test3", 
            "email": "test3@gmail.com"
         }

        response = self.client.post(
            '/accounts/',
            json.dumps(data),
            content_type='application/json',
            
        )
        print(response.json())
        self.assertEqual(201, response.status_code)
    
    def test_can_token_login(self):


        data = {"username": "test1", "password": "test1"}

        response = self.client.post(
            '/accounts/login/',
            json.dumps(data),
            content_type='application/json',
            
        )
        print(response.json())
        self.assertEqual(200, response.status_code)