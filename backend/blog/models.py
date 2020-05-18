from django.contrib.auth import get_user_model
from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from taggit.managers import TaggableManager


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(max_length=125)
    tags = TaggableManager()

    added = models.ManyToManyField(get_user_model(), related_name='bookmarks', blank=True)

    # TODO preview text, main image

    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    main_img = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f'Post: {self.title}'


class Meet(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    tags = TaggableManager()

    def __str__(self):
        return f'Meet({self.pk}): ({self.lat}; {self.lng})'
