from django.db import models


class Chat(models.Model):
    name = models.TextField()
    start_message = models.TextField(blank=True)
    api_key = models.TextField()


class Message(models.Model):
    text = models.TextField()
    author = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
