from django.db import models

# Create your models here.
class Location(models.Model):
    location_name=models.CharField(max_length=32)
    Address=models.CharField(max_length=32)
    latitude=models.FloatField()
    longitude=models.FloatField()
