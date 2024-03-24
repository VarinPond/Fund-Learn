from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
# Create your views here.
from django.http import HttpResponse
import time 
import json


def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

