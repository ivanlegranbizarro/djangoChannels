from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-field block w-full p-3 my-2 text-gray-700 bg-gray-200 rounded-md',
                                      'placeholder': 'Username'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-field block w-full p-3 my-2 text-gray-700 bg-gray-200 rounded-md',
                                          'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-field block w-full p-3 my-2 text-gray-700 bg-gray-200 rounded-md',
                                          'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
