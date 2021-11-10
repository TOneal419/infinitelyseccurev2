from django.shortcuts import render
from requests.models import Response
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
    
    
    # Testing between here

    def post(self, requests):
        return external_api_view(requests)

    # End of testing


    serializer_class = PwnSerializer


def external_api_view(request):
    if True:
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < 3:
            url = "https://haveibeenpwned.com/api/v3/breaches"
            payload = {'name':'Ahashare'}
            #r = requests.post(url, data = payload)
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                #print(data)                                             # WORKING !!!!! (just need to figure out how to print the stupid thing
                #return r
                return Response({"Name" : r})                               # NOT WORKING! says im giving 2 arguments (??)
            else:
                attempt_num += 1
                # You can probably use a logger to log the error here
                time.sleep(2)  # Wait for 5 seconds before re-trying
        return Response({"error": "Request failed"}, status=r.status_code)
