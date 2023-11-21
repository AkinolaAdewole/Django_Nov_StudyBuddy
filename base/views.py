from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


rooms = [
    {'id': 1, 'name': "Let us learn python"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Frontend developer"},
] 

def home(request):
    rooms= Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/index.html', context)

def room(request, pk):
    # room = None

    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get()
    
    context = {'room': room}
    return render(request,'base/room.html', context)

# Create your views here.
