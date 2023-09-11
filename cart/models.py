from django.db import models
from inventory.models import Product

# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product)
    product_name=models.CharField(max_length=32)
    product_price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    product_id=models.AutoField(primary_key=True)
    image=models.ImageField()
    date_added=models.DateField()

    pass
  



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

def __str__(self):
    return f"{self.quantity} x {self.product.name}"
