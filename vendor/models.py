from django.db import models


# Create your models here.
class Vender(models.Model):
    first_name=models.CharField(max_length=32)
    second_name=models.CharField(max_length=32)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=32)
   
