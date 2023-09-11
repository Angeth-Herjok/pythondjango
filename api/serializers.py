from rest_framework import serializers
from customers.models import Customers
from inventory.models import Product
from order.models import Order
from payment.models import Payment
from reviews.models import Reviews
from cart.models import Cart


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields= '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        models =Payment
        fields='__all__'     


class CartsSerializer(serializers.ModelSerializer):
      products=ProductSerializer(many=True)
      class Meta:
            model =Cart
            fields="__all__"

class CartSerializer(serializers.ModelSerializer):
      products=ProductSerializer(many=True)
      class Meta:
            model =Cart
            fields="__all__"