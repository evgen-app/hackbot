from django.db import models
from chat_models.models import Chat


class User(models.Model):
    username = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)
    tg_id = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return "User({}, {})".format(self.username, self.tg_id)


class UserChat(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Chat rel with {} chat and {} user".format(self.chat, self.user)

