from rest_framework import serializers
from base.models.AircraftModel import Aircraft


class AircraftSerializer(serializers.ModelSerializer):
    no_flights = serializers.IntegerField(read_only=True)

    class Meta:
        model = Aircraft
        fields = '__all__'

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.full_clean()
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.full_clean()
        instance.save()
        return instance
