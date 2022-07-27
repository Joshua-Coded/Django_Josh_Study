from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse('home page')

def room(request):
    return HttpResponse('ROOM')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/', room)
]
