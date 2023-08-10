from django.urls import path
from .views import delivery_view
from .views import delivery


urlpatterns = [
    path("deliveries/delivery/", delivery, name='delivery'),
    path("deliveries/deilvery_view", delivery_view, name='delivery_view'),
]