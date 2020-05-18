from django.urls import path
from rest_framework import routers

from blog.api.views import PostViewSet, TagViewSet

# from users.api.views import UserViewSet
from users.api.tokens import TokenCreate, TokenRefresh

app_name = 'api'

router = routers.DefaultRouter()
# router.register('users', UserViewSet, basename='user-api')

urlpatterns = [
    # path('users/<int:pk>', UserRetrieveView.as_view(), name='user'),
    path('token/', TokenCreate.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefresh.as_view(), name='token_refresh'),
] + router.urls

