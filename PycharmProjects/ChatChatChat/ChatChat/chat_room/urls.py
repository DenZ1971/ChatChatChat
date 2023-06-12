from django.contrib import admin
from django.urls import path


from chat_room.views import *

urlpatterns = [
    path("room/", Rooms.as_view(), name='room_list'),
    path('create/', Rooms.as_view(), name='create_room'),
    path('create/<int:pk>/delete/', Rooms.as_view(), name='delete_room'),
    path("dialog/", Dialog.as_view()),
    path('users/', AddUsersRoom.as_view()),
    path("", index, name="index"),
    path("<str:room_name>/", room, name="room"),
]
