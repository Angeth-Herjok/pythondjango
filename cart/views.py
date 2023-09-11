from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart


def cart(request):
    cart_items = Cart.objects.all()  # Replace this with your actual query to get cart items
    total_cart_price = sum(item.quantity * item.product_price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_cart_price': total_cart_price,  # Pass the total cart price to the template
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Check if the item is already in the cart
    cart_item, created = Cart.objects.get_or_create(
        product=product,
        defaults={
            'product_name': product.name,
            'product_price': product.price,
            'quantity': 1,  # You can set an initial quantity here
            'image': product.image,  # Assuming your Product model has an 'image' field
            'product_id':product.id,
            'date_added':product.date,
        }
    )

    # If the item is already in the cart, increment the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def remove_from_cart(request, id):
    # cart_item = get_object_or_404(Cart, pk=cart_item_id)
    cart_item=Cart.objects.get(id=id)
    cart_item.delete()
    return redirect('cart')











