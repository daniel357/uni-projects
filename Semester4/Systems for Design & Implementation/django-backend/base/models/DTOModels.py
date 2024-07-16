from django.db import models


class AirlineRevenueDTO(models.Model):
    airline_name = models.CharField(max_length=100)
    revenue = models.IntegerField()

    def __init__(self, airline_name, revenue):
        self.airline_name = airline_name
        self.revenue = revenue


class FlightPassengersDTO:
    def __init__(self, flight_id, passengers):
        self.flight_id = flight_id
        self.passengers = passengers
