from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import RoomForm
from .models import Room


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
