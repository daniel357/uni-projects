from django.db import models


class SkydiveJump(models.Model):
    title = models.CharField(max_length=200)
    canopy = models.CharField(max_length=200)
    plane = models.CharField(max_length=200)
    dropzone = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    altitude = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "jump"
