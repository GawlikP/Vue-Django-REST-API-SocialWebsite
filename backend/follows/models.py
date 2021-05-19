from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

from core.models import Account

class Follow(models.Model):
    follower = models.ForeignKey(Account, on_delete=CASCADE)
    following = models.ForeignKey(Account, on_delete=CASCADE, related_name='fallowing_account')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.follower.username + "->" + self.following.username

    class Meta:
        ordering = ['created']
