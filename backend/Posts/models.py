from django.db import models
from core.models import Account
# Create your models here.


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    title = models.CharField(max_length=512, blank=False)
    content = models.TextField(default='')
    hearts = models.IntegerField(default=0)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['created']

        

