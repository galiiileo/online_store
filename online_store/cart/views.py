from django.shortcuts import render,get_object_or_404
from .models import CartItem
from home.models import Product

def clear_cart(request):
    CartItem.objects.all().delete()
    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    w=CartItem()
    w.user=request.user
    w.product=get_object_or_404(Product,id=product_id)
    w.save()
    
    products_id=CartItem.objects.filter(user=request.user)
    products=Product.objects.filter(id__in=[item.product.id for item in products_id])
    return render(request, 'cart/cart.html', {'products': products})

def remove_from_cart(request, product_id):
    CartItem.objects.filter(user=request.user, product_id=product_id).delete()
    
    products_id=CartItem.objects.filter(user=request.user)
    products=Product.objects.filter(id__in=[item.product.id for item in products_id])
    return render(request, 'cart/cart.html', {'products': products})

def cart_view(request):
    
    products_id=CartItem.objects.filter(user=request.user)
    products=Product.objects.filter(id__in=[item.product.id for item in products_id])
    
    return render(request, 'cart/cart.html', {'products': products})