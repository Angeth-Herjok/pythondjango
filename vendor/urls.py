from django.urls import path
from .views import cart_view
from .views import add_to_cart


urlpatterns = [
    path("carts/add_to_cart/", add_to_cart, name='add_to_cart'),
    path("carts/cartview", cart_view, name='cart_view'),
]