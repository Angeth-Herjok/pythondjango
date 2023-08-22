from django.shortcuts import render
from .models import Vender

# Create your views here.
def vendor_list(request):
    vendors = Vender.objects.all()
    return render(request, 'vendor/vendor_list.html', {'vendors': vendors})
