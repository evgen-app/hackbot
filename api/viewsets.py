from rest_framework import viewsets, mixins
from users.models import User
from chat_models.models import Message, Chat
from .serializers import UserSerializer, MessageSerializer, ChatSerializer, ChatCreateWithTg, MessageCreateWithUsername, \
    AddUserToChatSerializer
from rest_framework.response import Response


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


class CreateChatFromTgViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ChatCreateWithTg


class MessageCreateWithUsernameViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = MessageCreateWithUsername


class AddUserToChatViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = AddUserToChatSerializer


class FromUsernameToUserViewset(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = AddUserToChatSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.get(username=pk)
        return Response({"tg_id": user.tg_id})


class FromTgIdToChats(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = AddUserToChatSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.get(tg_id=pk)
        return Response({"chats": [{"api_key": i.api_key, "name": i.name} for i in user.admin_chats.all()]})