from django.db import models

# Create your models here.
class Cart(models.Model):
    product_name=models.CharField(max_length=32)
    product_price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    product_id=models.AutoField(primary_key=True)
    image=models.ImageField()
    date_added=models.DateField()

