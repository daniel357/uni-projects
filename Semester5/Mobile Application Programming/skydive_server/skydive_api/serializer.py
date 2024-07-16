from rest_framework import serializers
from .models import SkydiveJump


class SkydiveJumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkydiveJump
        fields = ['id', 'title', 'canopy', 'plane', 'dropzone', 'datetime', 'altitude', 'description']
