from django.urls import path

from . import views

urlpatterns = [
    path('create-rooms/', views.create_rooms, name='create-rooms'),
    path('room/<slug:slug>/', views.room, name='room'),
]
