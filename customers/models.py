from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Customers(models.Model):
    # user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=32)
    second_name=models.CharField(max_length=32)
    gender=models.CharField(max_length=32)
    age=models.PositiveIntegerField()


 

