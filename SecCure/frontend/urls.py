
from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('learn', learn),
    path('pwn', pwn),
]
