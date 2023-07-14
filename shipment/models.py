from django.db import models

# Create your models here.
class Shipment(models.Model):
    tracking_number=models.CharField(max_length=32)
    status=models.CharField(max_length=32)
    date_created=models.DateTimeField(auto_now_add=True)
    date_shipped=models.DateTimeField(null=True, blank=True)




