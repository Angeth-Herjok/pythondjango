from django.urls import path
from .views import order_view
from .views import order


urlpatterns = [
    path("orders/order/", order, name='order'),
    path("orders/orders_view", order_view, name='order_view'),
]