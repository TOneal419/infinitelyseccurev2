from enum import unique
from django.db import models
from django.db.models.fields import TextField
import requests



# Create your models here.
class Pwn(models.Model):
    # TESTING
    # Name = models.TextField(max_length=50, default="", unique=False)
    id = models.PositiveBigIntegerField(primary_key=True)
    domainname = models.TextField(max_length=100, default="", unique=False)
    # BreachDate = models.DateField(auto_now_add=True)
    # Description = models.TextField(max_length=400, default="", unique=False)

    # BELOW IS ORIGINAL



    #email = models.EmailField(max_length=35,default="", unique=False)
    
    #created_at = models.DateTimeField(auto_now_add=True)
    #other entries returned by the api

    def __str__(self):
        return f"{self.domainname} {self.id}"

class Vtot(models.Model):
    Url = models.TextField(max_length = 50, default = "", unique = True)
    id = models.PositiveBigIntegerField(primary_key=True)
    def __str__(self):
        return f"{self.Url} {self.id}"
       
class TTS(models.Model):
    filename = models.TextField(max_length=30, default="mp1")
    scripts = models.TextField(default="No text")
    def __str__(self):
        return f"{self.filename} {self.scripts}"




