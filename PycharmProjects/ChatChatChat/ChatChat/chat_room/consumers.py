import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from accounts.models import User
from models import Room, Chat


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):

        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'username': username,'room': room,}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event['username']
        room = event['room']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, 'username': username,'room': room,}))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(sender=username)
        room = Room.objects.get(slug=room)

        Chat.objects.create(sender=user, room=room, message=message)