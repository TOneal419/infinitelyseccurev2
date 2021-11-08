
from django.urls import path
from .views import index
urlpatterns = [
    path('', index),
    path('learn',index),
    path('Pwn', index)
]