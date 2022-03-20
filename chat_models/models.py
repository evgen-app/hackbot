from django.db import models
from uuid import uuid1


class Chat(models.Model):
    name = models.TextField()
    start_message = models.TextField(blank=True)
    api_key = models.TextField()
    admin = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, related_name='admin_chats')
    tg_id = models.CharField(max_length=100, unique=True, default=uuid1)
    viewers = models.ManyToManyField("users.User", null=True, related_name='viewers_chats')


class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    tg_id = models.CharField(null=True, max_length=100)
