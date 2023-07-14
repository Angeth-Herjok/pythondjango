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


