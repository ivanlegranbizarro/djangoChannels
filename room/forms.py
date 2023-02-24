from django.forms import ModelForm, TextInput

from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'block w-full p-3 text-gray-700 bg-gray-200 rounded-lg focus:outline-none focus:bg-white focus:shadow-outline',
                'placeholder': 'Room Name',
            }),
        }
