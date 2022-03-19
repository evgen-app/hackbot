from rest_framework.serializers import ModelSerializer, Serializer, CharField, HyperlinkedModelSerializer, Field
from chat_models.models import Chat, Message
from users.models import UserChat, User
from rest_framework import viewsets


class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class UserChatSerializer(ModelSerializer):
    class Meta:
        model = UserChat
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        lookup_field = 'user__tg_id'


class UserHyperlinkedSerializer(HyperlinkedModelSerializer):
    user_tg = Field(source="user.tg_id")

    class Meta:
        model = User
        fields = "__all__"
        lookup_field = 'user_tg'


class MessageCreateWithUsername(Serializer):
    author_tg_nickname = CharField(write_only=True)
    message = CharField(write_only=True)
    chat_id = CharField(write_only=True)
    created_message = MessageSerializer(read_only=True)

    def create(self, validated_data):
        message = validated_data["message"]
        author_tg_nickname = validated_data["author_tg_nickname"]
        chat_id = validated_data["chat_id"]
        messageModel = Message.objects.create(
            text=message,
            author=User.objects.get(tg_id=author_tg_nickname),
            chat=Chat.objects.get(tg_id=chat_id),
        )
        return {
            "created_message": messageModel
        }


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    lookup_field = 'tg_id'
    queryset = User.objects.all()


class ChatCreateWithTg(Serializer):
    name = CharField(write_only=True)
    startMessage = CharField(write_only=True)
    api_key = CharField(write_only=True)
    tg_id = CharField(write_only=True)
    admin_tg_id = CharField(write_only=True)
    chat = ChatSerializer(read_only=True)

    def create(self, validated_data):
        name = validated_data['name']
        startMessage = validated_data['startMessage']
        api_key = validated_data['api_key']
        tg_id = validated_data['tg_id']
        admin_tg_id = validated_data['admin_tg_id']
        chat = Chat.objects.create(name=name,
                            start_message=startMessage,
                            api_key=api_key,
                            admin=User.objects.get(tg_id=admin_tg_id),
                            tg_id=tg_id)
        return {'chat': chat}