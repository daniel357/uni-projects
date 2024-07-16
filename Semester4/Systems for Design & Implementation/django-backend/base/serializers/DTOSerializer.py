from rest_framework import serializers
from base.models.DTOModels import AirlineRevenueDTO


class AirlineRevenueDTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirlineRevenueDTO
        fields = '__all__'
