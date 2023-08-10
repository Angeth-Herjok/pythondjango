from django.urls import path
from .views import reviews_view
from .views import reviews


urlpatterns = [
    path("reviewss/reviews/", reviews, name='reviews'),
    path("reviews/reviews_view", reviews_view, name='reviews_view'),
]