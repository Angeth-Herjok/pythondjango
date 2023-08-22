from django.db import models


# Create your models here.
class Vender(models.Model):
    image = models.ImageField(upload_to='vendor_images/', default='default_image.jpg')
    first_name=models.CharField(max_length=32)
    second_name=models.CharField(max_length=32)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=32)
   
