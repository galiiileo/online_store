from django.shortcuts import render
from home.models import Product
from .models import CartItem
products=set([])
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    products.add(product)
    return render(request, 'cart/cart.html', {'products': products})

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    products.remove(product)
    return render(request, 'cart/cart.html', {'products': products})

def cart_view(request):
    return render(request, 'cart/cart.html')
