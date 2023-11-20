from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html' )

def room(request):
    return render(request,'room.html')

# Create your views here.
