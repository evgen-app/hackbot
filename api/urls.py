from django.urls import path
from .views import ListCreateMessage, ListCreateChat, RetrieveUpdateMessage, RetrieveUpdateDestroyChat


urlpatterns = [
    path("chat", ListCreateChat.as_view()),
    path("message", ListCreateMessage.as_view()),
    path("chat/<pk>", RetrieveUpdateDestroyChat.as_view()),
    path("message/<pk>", RetrieveUpdateMessage.as_view())
]
