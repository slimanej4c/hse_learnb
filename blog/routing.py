# blog/routing.py
from django.urls import re_path
from .consumers import ChatConsumer

urlpatterns = [
    re_path(r'ws/blog/$', ChatConsumer.as_asgi()),
]

"""
il recupere les mesage en temps real mais il ne send pas et n oregistre pas les message dans le model message vosci mes fichiers
fichier chat.js 
import { useEffect, useState } from 'react';
import io from 'socket.io-client';
import axios from 'axios';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const socket = io('http://localhost:8000');  // Remplacez par l'URL de votre serveur Django

  useEffect(() => {
    // Charger les messages existants depuis le serveur
    axios.get('http://localhost:8000/blog/messages')
      .then(response => setMessages(response.data))
      .catch(error => console.error('Error fetching messages:', error));

    // Configurer le WebSocket
    socket.on('message', (data) => {
      setMessages(prevMessages => [...prevMessages, data.content]);
    });

    return () => {
      socket.disconnect();
    };
  }, [socket]);

  const sendMessage = () => {
    // Envoyer le message au serveur
    socket.emit('message', { content: newMessage });
    setNewMessage('');
  };

  return (
    <div className='chat' >
      <div>
        {messages.map((msg, index) => (
          <div key={index}>{msg.content}</div>
        ))}
      </div>
      <input
        type="text"
        value={newMessage}
        onChange={(e) => setNewMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Chat;

view django 
def get_messages(request):
    messages = Message.objects.all().values('content', 'timestamp')
    return JsonResponse(list(messages), safe=False)

models django
class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    consumer.py django 
    import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']

        # Sauvegarder le message dans la base de données ou effectuer toute autre logique
        # ...

        # Envoyer le message à tous les clients en temps réel
        await self.send(text_data=json.dumps({
            'content': content,
        }))

asgi.py django 
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import blog.routing
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

#application = get_asgi_application()

# mychat/asgi.py



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            blog.routing.websocket_urlpatterns
        )
    ),
})

fichier routing.py django
from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/blog/$', ChatConsumer.as_asgi()),
]
"""