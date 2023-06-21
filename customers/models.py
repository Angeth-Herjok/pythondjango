from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name=models.CharField(max_length=32)
    second_name=models.CharField(max_length=32)
    gender=models.CharField(max_length=32)
    age=models.PositiveIntegerField()
