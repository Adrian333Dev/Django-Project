from django.shortcuts import render
from .models import Room
# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn Python'},
#     {'id': 2, 'name': 'Designing a Django App'},
#     {'id': 3, 'name': 'Django Channels'},
# ]


def home(req):
    rooms = Room.objects.all()
    return render(req, 'base/home.html', {'rooms': rooms})


def room(req, pk):
    room = Room.objects.get(id=pk)
    return render(req, 'base/room.html', {'room': room})
