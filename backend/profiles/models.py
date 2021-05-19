from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
from core.models import Account
class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    note = models.TextField(max_length=512)
    account = models.OneToOneField(Account, on_delete=CASCADE)
    
    def __str__(self):
        return self.account.username + " " + self.note
    
    class Meta:
        ordering = ['created']