from django.urls import re_path

from skydive_api.consumer import SkydiveConsumer

websocket_urlpatterns = [
    re_path(r'ws/jumps/$', SkydiveConsumer.as_asgi()),
]
