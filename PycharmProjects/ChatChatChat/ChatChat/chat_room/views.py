from django.db.models import Q
from django.views import View
from django.views.generic import ListView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from accounts.models import User
from chat_room.models import Room, Chat
from chat_room.serializers import (RoomSerializers, ChatSerializers, ChatPostSerializers,  UserSerializer)


class Rooms(APIView):
    """Комнаты чата"""
    permission_classes = [IsAuthenticated,]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rooms_list.html'

    def get(self, request):
        rooms = Room.objects.filter(Q(creator=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        serializer = RoomSerializers()
        Room.objects.create(creator=request.user)
        return Response({"data": serializer.data})




class Dialog(APIView):
    """Диалог чата, сообщение"""
    permission_classes = [IsAuthenticated, ]
    # permission_classes = [permissions.AllowAny, ]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dialog.html'


    def get(self, request):
        room = request.GET.get("room")
        chat = Chat.objects.filter(room=room)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        # room = request.data.get("room")
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class AddUsersRoom(APIView):
    """Добавление юзеров в комнату чата"""
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get("room")
        user = request.data.get("user")
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)






def index(request):
    return render(request, "chat_room/index.html")

def room(request, room_name):
    return render(request, "chat_room/room.html", {"room_name": room_name})