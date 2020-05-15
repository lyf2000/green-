from django.urls import path
from rest_framework import routers

from blog.api.views import PostViewSet, TagViewSet
# from users.api.views import UserViewSet

app_name = 'api'


router = routers.DefaultRouter()
# router.register('users', UserViewSet, basename='user-api')

urlpatterns = [
    # path('users/<int:pk>', UserRetrieveView.as_view(), name='user'),
] + router.urls
