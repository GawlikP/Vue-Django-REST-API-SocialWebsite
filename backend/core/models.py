from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username, password=None):
        if not email:
            raise ValueError("Users must have an email!")
        if not username:
            raise ValueError("Users must have a usermane!")

        user = self.model(
            email=self.normalize_email(email),
            username= username,
            )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            email= username + "@gmail.com",
            password=password,
            username=username
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True 
        user.save(using=self.db)
        return user


class Account (AbstractBaseUser):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = MyAccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app):
           return True

   
    def __str__(self):
        return self.username
    class Meta:
        ordering = ['created']
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwags):
    if created:
        Token.objects.create(user=instance)



