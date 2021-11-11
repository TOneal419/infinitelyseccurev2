from django.urls import path
from .views import PwnView, VtotView

urlpatterns = [
    path('pwn', PwnView.as_view()),
    path("vt", VtotView.as_view()),
]