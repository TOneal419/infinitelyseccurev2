from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.serializers import Serializer
from .models import Pwn
from .serializers import PwnSerializer
import requests
import time
# Create your views here.


# Change to generics.listAPIview to get a full list of the database

class PwnView(generics.CreateAPIView):
    queryset = Pwn.objects.all()
    serializer_class = PwnSerializer
    
    # Testing between here

    def post(self, request):
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < 3:
            url = "https://haveibeenpwned.com/api/v3/breaches"
            #payload = {'name':'Ahashare'}
            #r = requests.post(url, data = payload)
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                #serializer_var = PwnSerializer(r.json())                
                return Response(r.json(), status=status.HTTP_200_OK)               # THIS IS WORKING! 
                #return Response(serializer_var.data, status=status.HTTP_200_OK)    # returning nothing (empty json)                                  
            else:
                attempt_num += 1
                # You can probably use a logger to log the error here
                time.sleep(2)  # Wait for 5 seconds before re-trying
        

    # End of testing


    
