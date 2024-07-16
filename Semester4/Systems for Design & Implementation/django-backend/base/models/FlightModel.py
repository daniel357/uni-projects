# Create your models here.
from django.db import models
from django.db.models import Avg, Count, Sum
from rest_framework.exceptions import ValidationError

from base.models.AircraftModel import Aircraft
from base.models.AirportModel import Airport


class Flight(models.Model):
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures', default=None)
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals', default=None)
    call_sign = models.CharField(max_length=20, null=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField()
    status = models.CharField(max_length=255)
    price = models.FloatField()
    seats_available = models.IntegerField()
    operating_aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='aircraft', null=True)

    def clean(self):
        if self.duration.total_seconds() <= 0:
            raise ValidationError('Flight duration must be greater than 0.')
        if self.departure_time >= self.arrival_time:
            raise ValidationError('Flight departure time must be earlier than the arrival time.')

    # tickets = models.ManyToManyField(Ticket, related_name='flights')

    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=["departure_airport", "id"]),
                   models.Index(fields=["departure_airport", "arrival_airport", "operating_aircraft"])]
