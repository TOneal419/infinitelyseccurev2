from django.shortcuts import render
from rest_framework import generics
from rest_framework.serializers import Serializer
from .models import Pwn
from .serializers import PwnSerializer
# Create your views here.

class PwnView(generics.ListAPIView):
    queryset = Pwn.objects.all()
    serializer_class = PwnSerializer