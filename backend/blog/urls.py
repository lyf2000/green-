from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import post_list, PostDetailView, map, p

app_name = 'blog'

urlpatterns = [
    # path('map/<int:pk>/', map, name='map'),
    # path('posts/', post_list, name='post-list'),
    # path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    # path('p/', p, name='p')
]
