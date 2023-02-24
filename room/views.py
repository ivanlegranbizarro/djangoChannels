from django.shortcuts import render

from .forms import RoomForm


def create_rooms(request):
    form = RoomForm()
    return render(request, 'create-rooms.html', {'form': form})
