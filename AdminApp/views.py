from django.shortcuts import render,redirect
from django.http import HttpResponse
from ClientApp.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")

def about (request):
    return render (request,"about.html")