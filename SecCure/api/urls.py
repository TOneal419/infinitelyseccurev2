from django.urls import path
from .views import PwnView, VtotView, TTSView

urlpatterns = [
    path('pwn', PwnView.as_view()),
    path("vt", VtotView.as_view()),
    path('tts', TTSView.as_view()),
]