from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(response):
    return HttpResponse('Home page')

def room(response):
    return HttpResponse('ROOM')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room),
]
