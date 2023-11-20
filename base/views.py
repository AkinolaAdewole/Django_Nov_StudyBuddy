from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id': 1, 'name': "Let us learn python"},
    {'id': 1, 'name': "Design with me"},
    {'id': 1, 'name': "Frontend developer"},
]

def home(request):
    return render(request, 'index.html', {'rooms': rooms})

def room(request):
    return render(request,'room.html')

# Create your views here.
