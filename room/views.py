from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import RoomForm
from .models import Room
from .models import Message


@login_required()
def create_rooms(request):
    rooms = Room.objects.all()
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            form = RoomForm()
    return render(request, 'create-rooms.html', {'form': form, 'rooms': rooms})


@login_required()
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'room.html', {'room': room, 'messages': messages})
