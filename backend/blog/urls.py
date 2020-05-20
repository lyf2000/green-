from django.urls import path

from .views import meet_create, post_create, meet_detail, MeetListView

app_name = 'blog'

urlpatterns = [
    path('meets/create', meet_create, name='meet-create'),
    path('meets/<int:pk>/', meet_detail, name='meet-detail'),
    path('meets/', MeetListView.as_view(), name='meet-list'),
    path('posts/create/', post_create, name='post-create'),
]
