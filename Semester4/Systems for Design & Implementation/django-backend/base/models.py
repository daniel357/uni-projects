# from datetime import timezone
#
# from django.db import models
#
# # Create your models here.
# from django.db import models
# from django.db.models import Avg, Count, Sum
# from rest_framework.exceptions import ValidationError
#
#
# class Airport(models.Model):
#     name = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     timezone = models.CharField(max_length=100)
#     elevation = models.IntegerField()
#     capacity = models.IntegerField()
#     noGates = models.IntegerField()
#     noTerminals = models.IntegerField()
#
#
# class Airline(models.Model):
#     name = models.CharField(max_length=100)
#     # logo = models.ImageField(upload_to='airlineLogos')
#     headquarters = models.CharField(max_length=100)
#     website = models.URLField()
#     establishedDate = models.DateField()
#     revenue = models.IntegerField()
#     numEmployees = models.IntegerField()
#
#
# class Aircraft(models.Model):
#     def clean(self):
#         if self.seatingCapacity <= 0:
#             raise ValidationError(
#                 'Aircraft seating capacity should be greater than or equal to the number of seats available on the flight.')
#
#     name = models.CharField(max_length=100)
#     manufacturer = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     maxSpeed = models.IntegerField()
#     seatingCapacity = models.IntegerField()
#     fuel_capacity = models.IntegerField()
#     wing_span = models.IntegerField()
#     length = models.IntegerField()
#     no_engines = models.IntegerField()
#     # flights = models.ManyToManyField('Flight')
#     airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE, default=None)
#
#
# class Flight(models.Model):
#     departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures', default=None)
#     arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals', default=None)
#     departure_time = models.DateTimeField()
#     arrival_time = models.DateTimeField()
#     duration = models.DurationField()
#     status = models.CharField(max_length=255)
#     price = models.FloatField()
#     seats_available = models.IntegerField()
#
#     def clean(self):
#         if self.duration.total_seconds() <= 0:
#             raise ValidationError('Flight duration must be greater than 0.')
#         if self.departure_time >= self.arrival_time:
#             raise ValidationError('Flight departure time must be earlier than the arrival time.')
#     # tickets = models.ManyToManyField(Ticket, related_name='flights')
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
#
# class Passenger(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     citizenship = models.CharField(max_length=100, default=None)
#
#
# class Ticket(models.Model):
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE, default=None)
#     passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, default=None)
#     seat_number = models.CharField(max_length=10)
#     booking_date = models.DateField()
#
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['flight', 'passenger'],
#                 name='unique_flight_passenger'
#             )
#         ]
#
#
# class AirlineRevenueDTO(models.Model):
#     airline_name = models.CharField(max_length=100)
#     revenue = models.IntegerField()
#
#     def __init__(self, airline_name, revenue):
#         self.airline_name = airline_name
#         self.revenue = revenue
#
#
# class FlightPassengersDTO:
#     def __init__(self, flight_id, passengers):
#         self.flight_id = flight_id
#         self.passengers = passengers
