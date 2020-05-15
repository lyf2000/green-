from rest_framework import viewsets

from blog.api.paginators import MyPaginator
from users.api.serializers import OtherUserSerializer
from users.models import User


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = OtherUserSerializer
#     pagination_class = MyPaginator
    # filter_backends = (SearchFilter, OrderingFilter, PostTagFilter)
    # filterset_fields = ('author', 'title')
    # search_fields = ('title',)
    # ordering_fields = ('created',)
    # ordering = ('-created',)
