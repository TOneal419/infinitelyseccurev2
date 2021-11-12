from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')

def learn(request, *args, **kwargs):
    return render(request, 'frontend/learn.html')

def pwn(request, *args, **kwargs):
    return render(request, 'frontend/pwn.html')
