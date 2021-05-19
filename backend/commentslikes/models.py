from django.db import models

# Create your models here.
from core.models import Account 
from comments.models import Comment 

class CommentLike(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment.id + ":" + self.account.username

    class Meta:
        ordering = ['created']