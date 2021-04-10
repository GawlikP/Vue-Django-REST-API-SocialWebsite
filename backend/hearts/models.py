from django.db import models

from core.models import Account

from Posts.models import Post

# Create your models here.


class Heart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


    def __str__(self):
        return self.post.title + ":" + self.account.username

    class Meta:
        ordering = ['created']