# Create your models here.
from django.db import models
from django.db.models import Avg, Count, Sum
from rest_framework.exceptions import ValidationError

from base.models.FlightModel import Flight
from base.models.PassengerModel import Passenger


class Ticket(models.Model):
    flight = models.ForeignKey(Flight, related_name='ticket_flight', on_delete=models.CASCADE, default=None)
    passenger = models.ForeignKey(Passenger, related_name='ticket_passenger', on_delete=models.CASCADE, default=None)
    seat_number = models.CharField(max_length=10)
    booking_date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['flight', 'passenger'],
                name='unique_flight_passenger'
            )
        ]

        ordering = ['id']
        indexes = [models.Index(fields=["flight", "passenger"])]
