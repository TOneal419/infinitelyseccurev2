from django.db import models

# Create your models here.
class Pwn(models.Model):
    email = models.EmailField(max_length=35,default="", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #other entries returned by the api

