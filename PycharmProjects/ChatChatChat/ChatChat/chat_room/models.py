from django.db import models

from accounts.models import User


class Room(models.Model):
    creator = models.ForeignKey(User, verbose_name="Chat creator", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Chat members", related_name="invited_user")
    date = models.DateTimeField("Data of creation", auto_now_add=True)

    class Meta:
        verbose_name = "Chat room"
        verbose_name_plural = "Chat rooms"


class Chat(models.Model):
    room = models.ForeignKey(Room, verbose_name="Chat room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Was sent", auto_now_add=True)

    class Meta:
        verbose_name = "Chat message"
        verbose_name_plural = "Chat messages"
