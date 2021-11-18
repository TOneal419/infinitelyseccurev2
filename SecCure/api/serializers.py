#transition code to json. from model 
from django.db.models import fields
from rest_framework import serializers
from .models import TTS, Pwn
from .models import Vtot

class PwnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pwn
        

        # Name = serializers.CharField(max_length=200)
        domainname = serializers.CharField(max_length=200)

        # BreachDate = serializers.DateField()
        # Description = serializers.CharField(max_length=500)

        fields = ('id', 'domainname')

       #fields = ('id', 'email','created_at') #add more fields as they are created


class VtotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vtot
        Url = serializers.CharField(max_length = 200)
        fields = ('id', "Url")


class TTSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTS
        filename = serializers.CharField(max_length = 30)
        scripts = serializers.CharField(max_length = 500)
        fields = ('filename', 'scripts')
