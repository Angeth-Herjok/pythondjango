from django.urls import path
from .views import contact_list
from .views import contact


urlpatterns = [
    path("contacts/contact/", contact, name='contact'),
    path("contacts/contact_list", contact_list, name='contact_list'),
]