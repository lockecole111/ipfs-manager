from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass

class File(models.Model):
    hash = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    time = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=32)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING)
