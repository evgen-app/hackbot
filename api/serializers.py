from rest_framework.serializers import ModelSerializer
from chat_models.models import Chat, Message


class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
