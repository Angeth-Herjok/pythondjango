from django.urls import path
from .views import shipment_list, create_shipment

urlpatterns = [
    path('', shipment_list, name='shipment_list'),
    path('create/', create_shipment, name='create_shipment'),
]
