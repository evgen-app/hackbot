from django.urls import path
from .views import ListCreateMessage, ListCreateChat, RetrieveUpdateMessage, RetrieveUpdateDestroyChat, \
    ListCreateUserChat, ListCreateUser, RetrieveUpdateUserChat, RetrieveUpdateUser, CreateMessageFromUsername, CreateChatWithUsername
from .serializers import UserViewSet
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, MessageViewSet, ChatViewSet

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('message', MessageViewSet, basename='message')
router.register('chat', ChatViewSet, basename='chat')

urlpatterns = [
    path("message-from-username", CreateMessageFromUsername.as_view()),
    path("chat-from-username", CreateChatWithUsername.as_view())
]
urlpatterns.extend(router.urls)
