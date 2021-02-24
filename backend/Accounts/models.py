from django.db import models

from datetime import datetime


# Create your models here.
class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)
    nick = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=512, blank=False)
    last_login = models.DateTimeField(default=datetime.now(), blank=True)
    token = models.CharField(max_length=512, default='')


    def __str__(self):
        return self.nick
    class Meta:
        ordering = ['created']