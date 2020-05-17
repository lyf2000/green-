from rest_framework import viewsets, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
    ordering_fields = ('-created',)
    ordering = ('-created',)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

#     TODO add permission
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def bookmark_post(request, pk):
    user = request.user
    res=user.bookmark_post(pk)
    return Response()
