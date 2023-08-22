from django.shortcuts import render
from .forms import LocationForm

# Create your views here.

def create_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LocationForm()
    return render(request, 'location/create_location.html', {'form': form})
