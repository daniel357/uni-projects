# # Create your models here.
# from django.db import models
# from django.db.models import Avg, Count, Sum
# from rest_framework.exceptions import ValidationError
#
# from base.models.AircraftModel import Aircraft
# from base.models.FlightModel import Flight
#
#
# class OperatingFlights(models.Model):
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE, default=None)
#     aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, default=None)
#     distance = models.IntegerField()
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['flight', 'aircraft'],
#                 name='unique_flight_aircraft'
#             )
#         ]
#
#         ordering = ['id']
#         indexes = [models.Index(fields=["flight", "aircraft"])]
