from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    follow = models.ManyToManyField('self', related_name='followers', null=True, blank=True)
