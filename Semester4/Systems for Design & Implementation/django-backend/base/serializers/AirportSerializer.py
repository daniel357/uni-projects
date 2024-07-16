from rest_framework import serializers
from base.models.AirportModel import Airport


class AirportSerializer(serializers.ModelSerializer):
    no_departing = serializers.IntegerField(read_only=True)

    class Meta:
        model = Airport
        fields = '__all__'
