from enum import unique
from django.db import models
from django.db.models.fields import TextField
import requests



# Create your models here.
class Pwn(models.Model):
    # TESTING
    Name = models.TextField(max_length=36, default="", unique=False)
    Domain = TextField(max_length=36, default="", unique=False)
    BreachDate = models.DateField(auto_now_add=True)
    Description = TextField(max_length=36, default="", unique=False)

    # BELOW IS ORIGINAL



    #email = models.EmailField(max_length=35,default="", unique=False)
    
    #created_at = models.DateTimeField(auto_now_add=True)
    #other entries returned by the api

    def __str__(self):
        return f"{self.email} {self.created_at}"


       





