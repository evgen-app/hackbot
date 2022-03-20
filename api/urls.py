from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, MessageViewSet, ChatViewSet, CreateChatFromTgViewSet, \
    MessageCreateWithUsernameViewSet, AddUserToChatViewSet, FromUsernameToUserViewset, FromTgIdToChats

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('message', MessageViewSet, basename='message')
router.register('chat', ChatViewSet, basename='chat')
router.register('chat-from-username', CreateChatFromTgViewSet, basename='chat-from-username')
router.register('message-from-username', MessageCreateWithUsernameViewSet, basename='message-from-username')
router.register('add-viewer-to-chat', AddUserToChatViewSet, basename='add-user-to-chat')
router.register('from-username-to-user', FromUsernameToUserViewset, basename='from-username-to-user')
router.register('from-tg-id-to-admin-chats', FromTgIdToChats, basename='from-tg-id-to-admin-chats')
urlpatterns = []
urlpatterns.extend(router.urls)
