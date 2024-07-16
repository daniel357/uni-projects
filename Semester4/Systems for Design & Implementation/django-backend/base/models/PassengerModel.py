
# Create your models here.
from django.db import models
from django.db.models import Avg, Count, Sum
from rest_framework.exceptions import ValidationError


class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=100, default=None)
    description = models.CharField(max_length=100, null=True)