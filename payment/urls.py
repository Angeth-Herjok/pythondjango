from django.urls import path
# from .views import payment_list
# from .views import payment
from . import views

urlpatterns = [
    # path("payments/payment/", payment, name='payment'),
    # path("payments/payment_list", payment_list, name='payment_list'),
    path('payment/list/', views.payment_list, name='payment_list'),
]
