# from rest_framework import serializers
# from base.models import *
#
# #
# # class AirlineRevenueDTOSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = AirlineRevenueDTO
# #         fields = '__all__'
#
#
# class AirportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Airport
#         fields = '__all__'
#
#
# class AirlineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Airline
#         fields = '__all__'
#
#
# class AircraftSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Aircraft
#         fields = '__all__'
#
#     def create(self, validated_data):
#         instance = self.Meta.model(**validated_data)
#         instance.full_clean()
#         instance.save()
#         return instance
#
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.full_clean()
#         instance.save()
#         return instance
#
#
# class PassengerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Passenger
#         fields = '__all__'
#
#
# class FlightSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Flight
#         fields = '__all__'
#
#     def create(self, validated_data):
#         instance = self.Meta.model(**validated_data)
#         instance.full_clean()
#         instance.save()
#         return instance
#
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.full_clean()
#         instance.save()
#         return instance
#
#
# class TicketSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ticket
#         fields = '__all__'
#
#
# class OperatingFlightsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OperatingFlights
#         fields = '__all__'
#
#
# class AirlineRevenueDTOSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AirlineRevenueDTO
#         fields = '__all__'
#
# # class MyAirlineSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Aircraft
# #         fields = '_all_'
# #
# #     def create(self, validated_data):
# #         if isinstance(validated_data, list):
# #             return [self.Meta.model.objects.create(**item_data) for item_data in validated_data]
# #
# #         else:
# #             return self.Meta.model.objects.create(**validated_data)
