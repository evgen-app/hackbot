from rest_framework.serializers import ModelSerializer, Serializer, CharField, HyperlinkedModelSerializer, Field, BooleanField
from chat_models.models import Chat, Message
from users.models import UserChat, User
from rest_framework import viewsets


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        depth = 1


class ChatSerializer(ModelSerializer):
    message_set = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = "__all__"
        depth = 1


class UserChatSerializer(ModelSerializer):

    class Meta:
        model = UserChat
        fields = "__all__"
        depth = 1


class UserSerializer(ModelSerializer):
    admin_chats = ChatSerializer(many=True, required=False, read_only=True)
    viewers_chats = ChatSerializer(many=True, required=False, read_only=True)

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
    message_id = CharField(write_only=True)
    created_message = MessageSerializer(read_only=True)

    def create(self, validated_data):
        message = validated_data["message"]
        author_tg_nickname = validated_data["author_tg_nickname"]
        chat_id = validated_data["chat_id"]
        message_id = validated_data["message_id"]
        messageModel = Message.objects.create(
            text=message,
            author=User.objects.get(tg_id=author_tg_nickname),
            chat=Chat.objects.get(tg_id=chat_id),
            tg_id=message_id
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
    start_message = CharField(write_only=True)
    api_key = CharField(write_only=True)
    tg_id = CharField(write_only=True)
    admin_tg_id = CharField(write_only=True)
    chat = ChatSerializer(read_only=True)

    def create(self, validated_data):
        name = validated_data['name']
        startMessage = validated_data['start_message']
        api_key = validated_data['api_key']
        tg_id = validated_data['tg_id']
        admin_tg_id = validated_data['admin_tg_id']
        print(name, startMessage, api_key, tg_id, admin_tg_id)
        chat = Chat.objects.create(name=name,
                            start_message=startMessage,
                            api_key=api_key,
                            admin=User.objects.get(tg_id=admin_tg_id),
                            tg_id=tg_id)
        return {'chat': chat}


class AddUserToChatSerializer(Serializer):
    chat_tg_id = CharField(write_only=True)
    user_tg_id = CharField(write_only=True)

    added = BooleanField(read_only=True)

    def create(self, validated_data):
        chat_tg_id = validated_data['chat_tg_id']
        user_tg_id = validated_data['user_tg_id']

        Chat.objects.get(tg_id=chat_tg_id).viewers.add(User.objects.get(tg_id=user_tg_id))
        print(Chat.objects.get(tg_id=chat_tg_id), User.objects.get(tg_id=user_tg_id))
        return {"added": True}


class FromUsernameToTgSerializer(Serializer):
    username = CharField(write_only=True)
    user = UserSerializer(read_only=True)

    def create(self, validated_data):
        username = validated_data["username"]
        user = User.objects.get(username=username)
        return {"user": user}
