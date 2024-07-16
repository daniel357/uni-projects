from rest_framework import serializers
from base.models.AirlineModel import Airline


class AirlineSerializer(serializers.ModelSerializer):
    no_aircrafts = serializers.IntegerField(read_only=True)

    class Meta:
        model = Airline
        fields = '__all__'
