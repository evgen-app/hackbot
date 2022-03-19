from rest_framework import viewsets
from users.models import User
from chat_models.models import Message, Chat
from .serializers import UserSerializer, MessageSerializer, ChatSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = 'tg_id'
    queryset = User.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    lookup_field = 'tg_id'
    queryset = Message.objects.all()


class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    lookup_field = 'tg_id'
    queryset = Chat.objects.all()
