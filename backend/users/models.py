from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    follow = models.ManyToManyField('self', related_name='followers', null=True, blank=True)

    def bookmark_post(self, post_id):
        try:
            self.bookmarks.get(id=post_id)
            self.bookmarks.remove(post_id)
        except Exception as e:
            self.bookmarks.add(post_id)
        return True
