from django.db import models
# from basket.models import Basket
from cart.models import Cart
from customers.models import Customers
from shipment.models import Shipment

# Create your models here.
class Order(models.Model):
    
    purchaser_name=models.CharField(max_length=32)
    purchaser_number=models.CharField(max_length=32)
    vender_name=models.CharField(max_length=32)
    vender_number=models.CharField(max_length=32)
    product_description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=6)
    quantity=models.PositiveIntegerField()
    

    cart=models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    customers=models.OneToOneField(Customers, null=True, on_delete=models.CASCADE)
    shipment=models.ManyToManyField(Shipment, null=True, blank=True)

   