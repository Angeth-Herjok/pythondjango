from django.urls import path
from .views import shipment_view
from .views import shipment


urlpatterns = [
    path("shipments/shipment/", shipment, name='shipment'),
    path("shipments/shipment_view", shipment_view, name='shipment_view'),
]