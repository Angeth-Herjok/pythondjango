from django.urls import path
from .views import create_location

urlpatterns = [
    path('create/', create_location, name='create_location'),
]
