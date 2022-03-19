from django.db import models


class Chat(models.Model):
    name = models.TextField()
    start_message = models.TextField(blank=True)
    api_key = models.TextField()
    admin = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    tg_id = models.CharField(max_length=100, null=True)


class Message(models.Model):
    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    tg_id = models.CharField(null=True, max_length=100)
