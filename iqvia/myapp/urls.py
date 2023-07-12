from django.urls import path
from .views import chat_interface

urlpatterns = [
    path('chat-interface/', chat_interface, name='chat_interface'),
]