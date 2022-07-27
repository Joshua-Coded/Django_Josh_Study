from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home page')

def room(request):
    return HttpResponse('ROOM')
