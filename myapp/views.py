from django.shortcuts import render
from .models import ChatRoom, ChatMessage

# Create your views here.
def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'myapp/index.html', {'chatrooms':chatrooms})

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)[0:30]
    return render(request, 'myapp/room.html', {'chatroom': chatroom, 'messages': messages})
