from django.shortcuts import render
from django.http import HttpResponse


def home(response):
    return HttpResponse('Home page')

def room(response):
    return HttpResponse('ROOM')

# Create your views here.
