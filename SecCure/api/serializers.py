#transition code to json. from model 
from django.db.models import fields
from rest_framework import serializers
from .models import Pwn

class PwnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pwn
        

        Name = serializers.CharField(max_length=200)
        Domain = serializers.CharField(max_length=200)
        BreachDate = serializers.DateField()
        Description = serializers.CharField(max_length=500)

        fields = ('Name', 'Domain', 'BreachDate', 'Description')

       #fields = ('id', 'email','created_at') #add more fields as they are created