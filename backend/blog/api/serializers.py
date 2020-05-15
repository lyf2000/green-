from rest_framework import serializers
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
from blog.models import Post
from users.api.serializers import OtherUserSerializer


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = OtherUserSerializer()

    class Meta:
        model = Post
        fields = ('author', 'title', 'tags', 'text')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
