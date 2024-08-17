from django.urls import path
from .views import *


urlpatterns = [
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('home', home, name='home'),
    path('user_profile', user_profile, name='user_profile'),
    path('user_logout', user_logout, name='user_logout')
]
