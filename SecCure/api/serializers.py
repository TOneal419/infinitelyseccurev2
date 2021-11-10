#transition code to json. from model 
from django.db.models import fields
from rest_framework import serializers
from .models import Pwn

class PwnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pwn
        fields = ('Name', 'Domain', 'BreachDate', 'Description')
        #fields = ('id', 'email','created_at') #add more fields as they are created