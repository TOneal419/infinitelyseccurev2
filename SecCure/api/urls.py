from django.urls import path
from .views import PwnView

urlpatterns = [
    path('pwn', PwnView.as_view()),
]