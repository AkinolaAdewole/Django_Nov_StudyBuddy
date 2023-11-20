from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id': 1, 'name': "Let us learn python"},
    {'id': 2, 'name': "Design with me"},
    {'id': 3, 'name': "Frontend developer"},
] 

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/index.html', context)

def room(request, pk):
    room = None

    for i in rooms:
        if i['id'] == int(pk):
            room = 1
    context = room
    return render(request,'base/room.html', context)

# Create your views here.
