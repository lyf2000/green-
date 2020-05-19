from django.contrib import admin
from django.urls import path, re_path
from users.views import signup, activate, reset

app_name = 'users'

urlpatterns = [
    # path('', index, name='index'),
    re_path(r'^signup/$', signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='activate'),
    path('reset', reset, name='reset')
]
