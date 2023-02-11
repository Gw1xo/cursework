from django.urls import path, re_path, include

from .views import *

app_name = 'users'

urlpatterns = [
    path('', main_page, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register')
]
