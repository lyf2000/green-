from django.urls import path

from .views import meet_create, post_create

app_name = 'blog'

urlpatterns = [
    path('meet/create', meet_create, name='meet-create'),
    path('post/create/', post_create, name='post-create')
]
