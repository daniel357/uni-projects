from channels.generic.websocket import AsyncWebsocketConsumer
import json


class SkydiveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("skydive_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("skydive_group", self.channel_name)

    async def skydive_update(self, event):
        # Send the message to WebSocket
        if event.get("sender_ip") != self.scope["client"][0]:
            await self.send(text_data=json.dumps(event["message"]))
