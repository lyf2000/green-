from rest_framework import serializers
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from blog.models import Post
from users.api.serializers import OtherUserSerializer


class PostCreateSerializer(serializers.ModelSerializer):
    author = OtherUserSerializer(required=False)

    class Meta:
        model = Post
        fields = [
            'text', 'title',
            'author']

    def create(self, validated_data):
        return Post.objects.create(
            **validated_data,
            author_id=1
        )


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    author = OtherUserSerializer(required=False, read_only=True)
    created = serializers.DateTimeField(format="%a, %b %Y", required=False)
    marked = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'tags', 'text', 'created', 'marked')

    def get_marked(self, obj):
        return 'false'
        # return 'true'

    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(
            **validated_data,
            author=user
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
