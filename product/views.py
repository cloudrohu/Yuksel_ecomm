from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def index(request):
   return  HttpResponse("My Product Page")