from django.shortcuts import render
from rest_framework.views import APIView
from customers.models import Customers
from .serializers import CustomersSerializer, ProductSerializer, CartSerializer,OrderSerializer,CartsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from inventory.models import Product
from cart.models import Cart
from order.models import Order


class CustomersListView(APIView):
    def get(self, request):
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many = True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CustomersSerializer(data = request.data)    
        if serializer.is_valid():
            serializer.save
            return Response (serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            


class CustomersDetailView(APIView):
    def get(self, request, id, format = None):
        client = Customers.objects.get(id = id)
        serializer = CustomersSerializer(client)
        return Response(serializer.data)


    def put(self, request, id, format = None):
        customers = Customers.objects.get(id = id)
        serializer = CustomersSerializer(client, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status = status.HTTP_201_CREATED)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format = None):
        customers = Customers.objects.get(id = id)
        customers.delete()
        return Response("customer deleted", status = status.HTTP_204_CONTENT)     
     












class ProductListView(APIView):
    def get(self,request):
       product = Product.objects.all()
       serializer = ProductSerializer(product,many=True)
       return Response(serializer.data , status=status.HTTP_200_OK)
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400)

class ProductDetailView(APIView):
    def get(self,request,id,format=None):
         product=Product.objects.get(id=id)
         serializer=ProductSerializer(product)
         return Response(serializer.data)
    def put(self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400)
    def delete(self,request,id,format=None):
        product=Product.objects.get(id=id)
        product.delete()
        return Response(" product Deleted", status=status.HTTP_204_No_CONTENT)

class CartListView(APIView):
    def get(self,request):
       cart=Cart.objects.all()
       serializer = CartSerializer(cart,many=True)
       return Response(serializer.data , status=status.HTTP_200_OK)
    def post(self,request):
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400)
        
class CartDetailView(APIView):
    def get(self,request,id,format=None):
         cart=Cart.objects.get(id=id)
         serializer=CartSerializer(cart)
         return Response(serializer.data)
    def put(self,request,id,format=None):
        cart=Cart.objects.get(id=id)
        serializer=CartSerializer(cart,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400)
    def delete(self,request,id,format=None):
        cart=Cart.objects.get(id=id)
        cart.delete()
        return Response(" Cart Deleted", status=status.HTTP_204_No_CONTENT)

class OrderListView(APIView):
    def get(self,request):
       order = Order.objects.all()
       serializer = OrderSerializer(order,many=True)
       return Response(serializer.data , status=status.HTTP_200_OK)
    def post(self,request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400)

class OrderDetailView(APIView):
    def get(self,request,id,format=None):
         order=Order.objects.get(id=id)
         serializer=OrderSerializer()
         return Response(serializer.data)
    def put(self,request,id,format=None):
        order=Order.objects.get(id=id)
        serializer=OrderSerializer(order,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors,status=status.HTTP_400)
    def delete(self,request,id,format=None):
        order=Order.objects.get(id=id)
        order.delete()
        return Response(" Order Deleted", status=status.HTTP_204_No_CONTENT)





class AddtoCartView(APIView):
     def post(self,request,id,format=None):
        cart_id=request.data["cart_id"]
        product_id=request.data["product_id"]
        cart=Cart.objects.get(id=cart_id)
        product=Product.objects.get(id=product_id)
        updated_cart=Cart.add_product(product)
        serializers=CartsSerializer(updated_cart)
        return Response(serializers.data)


class RemoveProductView(APIView):
     def delete(self,request,id,format=None):
        cart_id=request.data["cart_id"]
        product_id=request.data["product_id"]
        cart=Cart.objects.get(id=cart_id)
        product=Product.objects.get(id=product_id)
        updated_cart=Cart.delete_product(product)
        serializer=CartsSerializer(updated_cart)
        return Response(serializer.data)

class CheckoutView(APIView):
     def put(self,request,id,format=None):
        cart_id=request.data["cart_id"]
        order_id=request.data["order_id"]
        cart=Cart.objects.get(id=cart_id)
        order=Order.objects.get(id=order_id)
        updated_cart=Cart.create_order(order)
        serializer=CartsSerializer(updated_cart)
        return Response(serializer.data)