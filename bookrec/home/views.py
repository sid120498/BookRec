from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    if request.method =='GET':
        return render(request,'home/home.html')