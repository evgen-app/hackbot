from .serializers import ChatSerializer, MessageSerializer
from chat_models.models import Chat, Message
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateMessage(ListCreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class ListCreateChat(ListCreateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class RetrieveUpdateMessage(RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class RetrieveUpdateDestroyChat(RetrieveUpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
