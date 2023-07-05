from django.db import models

# Create your models here.
class Order(models.Model):
    purchaser_name=models.CharField(max_length=32)
    purchaser_number=models.CharField(max_length=32)
    vender_name=models.CharField(max_length=32)
    vender_number=models.CharField(max_length=32)
    product_description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=6)
    quantity=models.PositiveIntegerField()
    
