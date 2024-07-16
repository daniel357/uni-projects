
# Create your models here.
from django.db import models
from django.db.models import Avg, Count, Sum
from rest_framework.exceptions import ValidationError


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)
    elevation = models.IntegerField()
    capacity = models.IntegerField()
    no_gates = models.IntegerField()
    no_terminals = models.IntegerField()