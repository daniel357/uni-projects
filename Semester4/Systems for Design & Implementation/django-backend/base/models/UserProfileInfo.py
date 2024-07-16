import better_profanity
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


def validate_positive(value):
    if value < 0:
        raise ValidationError('%(value)s is not a positive number.',
                              params={'value': value})


def validate_gender(value):
    if value != 'M' and value != 'F' and value != 'O':
        raise ValidationError(
            "gender can only be described as 'M' - male, 'F' - female or 'O' - other",
            params={'value': value})


def validate_no_profanity(value):
    if better_profanity.profanity.contains_profanity(value):
        raise ValidationError('No profanity allowed!', params={'value': value})


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    bio = models.TextField(max_length=500,
                           blank=True,
                           validators=[validate_no_profanity])
    age = models.IntegerField(null=True,
                              blank=True,
                              validators=[validate_positive])
    gender = models.CharField(max_length=1,
                              blank=True,
                              validators=[validate_gender])
    nationality = models.CharField(max_length=100, blank=True)
    confirmation_code = models.CharField(max_length=12, blank=True)
    confirmation_code_valid_until = models.DateTimeField(null=True, blank=True)
