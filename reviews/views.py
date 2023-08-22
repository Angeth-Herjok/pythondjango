from django.shortcuts import render
from .models import Reviews

# Create your views here.

def review_list(request):
    reviews = Reviews.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

