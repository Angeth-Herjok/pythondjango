from django.shortcuts import render
from .forms import ProductUploadForm
from .models import Product

# Create your views here.

def product_upload_view(request):
    form = ProductUploadForm()
    return render(request, "inventory/product_upload.html",
                  {"form": form})
    if request_method =="POST":
        form =ProductUploadForm(request.POST)
        if form .is_valid():
            form.save()
    else:
          form=ProductUploadForm()
    return render (request,"inventory/product_upload.html",
                   {"form" :form}
)

def product_list(request):
    products=Product.objects.all()
    return render(request, "inventory/products_list.html",
    {"products": products})

def product_detail(request, id):
    product=Product.objects.get(id=id)
    return render(request, "inventory/product_detail.html",
    {"product": product})
