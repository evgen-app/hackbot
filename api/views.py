from .serializers import ChatSerializer, MessageSerializer, UserSerializer, UserChatSerializer, \
    MessageCreateWithUsername, UserHyperlinkedSerializer, ChatCreateWithTg
from chat_models.models import Chat, Message
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from users.models import User, UserChat


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


class ListCreateUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserHyperlinkedSerializer


class ListCreateUserChat(ListCreateAPIView):
    queryset = UserChat.objects.all()
    serializer_class = UserHyperlinkedSerializer


class RetrieveUpdateUserChat(RetrieveUpdateAPIView):
    queryset = UserChat.objects.all()
    serializer_class = UserHyperlinkedSerializer


class RetrieveUpdateUser(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateMessageFromUsername(CreateAPIView):
    serializer_class = MessageCreateWithUsername


class CreateChatWithUsername(CreateAPIView):
    serializer_class = ChatCreateWithTg