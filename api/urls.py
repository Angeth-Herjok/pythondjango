from django.urls import path
from.views import CustomersListView
from .views import CustomersDetailView
from .views import ProductDetailView
from .views import ProductListView
from .views import CartDetailView
from .views import CartListView
from .views import OrderDetailView
from .views import OrderListView
from .views import AddtoCartView, RemoveProductView, CheckoutView



urlpatterns = [
    path("customers/", CustomersListView.as_view(), name = "customers_list_view"),
    path("customers/<int:id>/", CustomersDetailView.as_view(), name = "customers_detail_view"),
    
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),

   
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<int:id>/', CartDetailView.as_view(), name='cart-detail'),

   
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:id>/', OrderDetailView.as_view(), name='order-detail'),

    path('add-to-cart/', AddtoCartView.as_view(), name='add-to-cart'),

    path('remove-product/', RemoveProductView.as_view(), name='remove-product'),

    path('checkout/', CheckoutView.as_view(), name='checkout'),



    
    

]




