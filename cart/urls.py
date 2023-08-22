# from django.urls import path
# from .views import cart_view
# from .views import add_to_cart



# urlpatterns = [
#     path("carts/upload/", add_to_cart, name='add_to_cart'),
#     path("carts/cart_view/", cart_view, name='cart_view'),
    
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:product_id>/', views.delete_from_cart, name='delete_from_cart'),
    
]

