from django.db import models
from core.models import Account
from Posts.models import Post
# Create your models here.

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    content = models.TextField()
    likes = models.IntegerField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['created']
