# Create your models here.
from django.db import models
from user.models import User

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey('user.User', related_name='post', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('created',)


