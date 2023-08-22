from django.shortcuts import render, redirect
from .models import Shipment
from .forms import ShipmentForm

# Create your views here.

def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request, 'shipments/shipment_list.html', {'shipments': shipments})

def create_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shipment_list')
    else:
        form = ShipmentForm()
    return render(request, 'shipment/create_shipment.html', {'form': form})

