
# Create your models here.
from django.db import models
from django.db.models import Avg, Count, Sum
from rest_framework.exceptions import ValidationError


class Airline(models.Model):
    name = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)
    website = models.URLField()
    established_date = models.DateField()
    revenue = models.IntegerField()
    num_employees = models.IntegerField()
