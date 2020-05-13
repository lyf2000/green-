from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from taggit.models import Tag

from blog.api.filters import PostTagFilter
from blog.api.paginators import MyPaginator
from blog.api.serializers import PostSerializer, TagSerializer
from blog.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = MyPaginator
    filter_backends = (SearchFilter, OrderingFilter, PostTagFilter)
    # filterset_fields = ('author', 'title')
    search_fields = ('title',)
    ordering_fields = ('created',)
    ordering = ('-created',)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
