# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
# chat/consumers.py
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']

        # Sauvegarder le message dans la base de données
        Message.objects.create(content=content)

        # Envoyer le message à tous les clients en temps réel
        await self.send(text_data=json.dumps({
            'content': content,
        }))
