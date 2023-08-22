# from django.shortcuts import render, redirect
# from .models import Cart
# from .forms import CartForm

# def cart_view(request):
#     cart_items = Cart.objects.all()
#     return render(request, 'cart/cart_view.html', {'cart_items': cart_items})



# def add_to_cart(request):
#     cart_items = Cart.objects.all()

#     if request.method == 'POST':
#         form = CartForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("cart_view")  
#     else:
#         form = CartForm()

#     return render(request, "cart/add_to_cart.html", {'form': form})
from django.shortcuts import render, redirect
from .models import Cart, Product
from .forms import AddToCartForm

def cart(request):
    cart_items = Cart.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = Cart.objects.get_or_create(
                product=product,
                defaults={
                    'product_name': product.name,
                    'product_price': product.price,
                    'quantity': quantity,
                    'image': product.image,
                }
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            return redirect('cart')
    else:
        form = AddToCartForm()
    return render(request, 'add_to_cart.html', {'form': form, 'product': product})




def delete_from_cart(request, product_id):
    if request.method == 'POST':
        cart_item = Cart.objects.get(product_id=product_id)
        cart_item.delete()
        return redirect('cart')
        











