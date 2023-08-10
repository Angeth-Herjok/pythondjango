from django.urls import path
from .views import location_view
from .views import location


urlpatterns = [
    path("location/location_view/", location_view, name='location_view'),
    path("location/location", location, name='location'),
]