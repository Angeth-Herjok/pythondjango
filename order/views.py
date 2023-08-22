from django.shortcuts import render
from .forms import OrderForm

# Create your views here.

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'form': form})
