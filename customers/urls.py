from django.urls import path
from .views import customer_list
from .views import customer


urlpatterns = [
    path("customers/customer/", customer, name='customer'),
    path("customers/customer_list", customer_list, name='customer_list'),
]