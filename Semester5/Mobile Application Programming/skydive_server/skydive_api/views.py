from rest_framework import generics
from .models import SkydiveJump
from .serializer import SkydiveJumpSerializer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class JumpListCreateView(generics.ListCreateAPIView):
    queryset = SkydiveJump.objects.all()
    serializer_class = SkydiveJumpSerializer

    def perform_create(self, serializer):
        serializer.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "jumps_group",
            {
                "type": "jump_update",
                "sender_ip": get_client_ip(self.request),
                "message": {
                    "action": "create",
                    "jump": serializer.data
                }
            }
        )


class JumpRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SkydiveJump.objects.all()
    serializer_class = SkydiveJumpSerializer

    def perform_update(self, serializer):
        serializer.save()
        # Notify via WebSocket after updating a jump
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "jumps_group",
            {
                "type": "jump_update",
                "sender_ip": get_client_ip(self.request),
                "message": {
                    "action": "update",
                    "jump": serializer.data
                }
            }
        )

    def perform_destroy(self, instance):
        # Notify via WebSocket before deleting a jump
        channel_layer = get_channel_layer()
        jump_data = SkydiveJumpSerializer(instance).data
        instance.delete()
        async_to_sync(channel_layer.group_send)(
            "jumps_group",
            {
                "type": "jump_update",  # Update the type
                "sender_ip": get_client_ip(self.request),
                "message": {
                    "action": "delete",
                    "jump": jump_data  # Change the key to 'jump'
                }
            }
        )
