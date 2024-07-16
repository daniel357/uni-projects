# Create your models here.
from django.db import models
from django.db.models import Avg, Count, Sum
from rest_framework.exceptions import ValidationError

from base.models.AirlineModel import Airline


class Aircraft(models.Model):
    def clean(self):
        if self.seating_capacity <= 0:
            raise ValidationError(
                'Aircraft seating capacity should be greater than or equal to the number of seats available on the flight.')

    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    max_speed = models.IntegerField()
    seating_capacity = models.IntegerField()
    fuel_capacity = models.IntegerField()
    wing_span = models.IntegerField()
    length = models.IntegerField()
    no_engines = models.IntegerField()
    airline_name = models.ForeignKey(Airline, related_name='airlines', on_delete=models.CASCADE, default=None)

    class Meta:
        ordering = ['id']
        indexes = [models.Index(fields=["airline_name"])]
