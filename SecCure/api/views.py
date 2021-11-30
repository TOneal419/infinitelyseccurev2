from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.serializers import Serializer
from .models import Pwn, Vtot, TTS
from .serializers import PwnSerializer, VtotSerializer, TTSSerializer
import requests
import time
import json
import vt
from .voicerss_tts import *
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
            payload = {}
            #r = requests.post(url, data = payload)
            if (request.data['domainname'] != "") :
                payload = {'domain': request.data['domainname']}
            else:
                payload = {'domain': 'adobe.com'} 
            r = requests.get(url, params=payload)
            if r.status_code == 200:
                data = r.json()
                #print (r.json()[0])
                list_holder = []
                serializer_var = {}
                serializer_var.update({"Name": data[0]['Name'], "Domain" : data[0]['Domain'], "Description": data[0]['Description'], "BreachDate": data[0]['BreachDate']})
            
                list_holder.append(serializer_var)
               # print (serializer_var)
                list = json.dumps(list_holder)
                list2 = json.loads(list)
                #serializer_var = PwnSerializer(r.json())                
                return Response(list2, status=status.HTTP_200_OK)               # THIS IS WORKING! 
                #return Response(serializer_var.data, status=status.HTTP_200_OK)    # returning nothing (empty json)                                  
            else:
                attempt_num += 1
                # You can probably use a logger to log the error here
                time.sleep(2)  # Wait for 5 seconds before re-trying
        

    # End of testing

class VtotView(generics.CreateAPIView):
    queryset = Vtot.objects.all()
    serializer_class = VtotSerializer

    def post(self, request):
        my_api_key = "dffa53b364bfea34d474c326cf33101f6647b2e5ea89812664d94bd71f6a94fd"
        client = vt.Client(my_api_key)
        url_string = "http://www.virustotal.com"
        # url_id = vt.url_id(request.data['Url'])

        url_id = vt.url_id(request.POST.get('Url', 'www.google.com'))

        url = client.get_object("/urls/{}", url_id)
        # print ('$')

        # print (request.data['Url'])
        # print(url.times_submitted)
        # print ('$')
        # print(url.last_analysis_stats)
        # print ('$')
        var = {"submitted" : url.times_submitted, "Stats" : url.last_analysis_stats, 'Data': url.last_analysis_results}

        list = var
        lists = json.dumps(list)
        list2 = json.loads(lists)
        client.close()
        return Response(list2, status=status.HTTP_200_OK)


class TTSView(generics.CreateAPIView):
    queryset = TTS.objects.all()
    serializer_class = TTSSerializer
 
    def post(self, request):
        res = "Failure"
        stat = 400
       
        try:
            fi = "frontend\\static\\mp3\\"
            file = fi + request.data['filename'] + ".mp3"
            
           
            urlVoice = 'https://api.voicerss.org/?'
            hl = 'en-us'
            script = request.data['scripts']
            print (script)

            voice = speech(
            {
                    'key' : '5eba043727a84c0c94631a2848250a6d',
                    'src' : script,
                    'hl'  : 'en-us',
                    'v'   : 'Mary',
                    'r'   : '0',
                    'f'   : '44khz_16bit_stereo',
                    'c' : "mp3",
                    'b64' : 'false',
                    'ssml' : 'false',
                   
            }
            )
            stat = 401
            data3 = (voice['response'])
            # play_buffer (audio__data support the buffer interface, num_channels, bytes per sample, sample rate in Hz)
            with open(file, 'wb+') as f:
                    f.write(data3)
            res = file
            stat = 200
 
        except Exception as e:
            print (e)
            # res = voice['error']
            res = "Failed to send data for some reason"
            # status = 400
       
        var = {'File' : res, 'Status' : stat}
        list = json.dumps(var)
        list2 = json.loads(list)
 
        return Response(list2, status = stat)
