from django.urls import path
from .views import *


urlpatterns = [
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('home', home, name='home'),
]
