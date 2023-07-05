from django.db import models

# Create your models here.
class Delivery(models.Model):
    company_name=models.CharField(max_length=32)
    shipper=models.CharField(max_length=32)
    recipient_name=models.CharField(max_length=32)
    delivery_order_number=models.CharField(max_length=32)
