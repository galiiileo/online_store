from django.shortcuts import render,get_object_or_404
from .models import Wishlist
from home.models import Product
from accounts.models import User
# products=set([])
def add_to_wishlist(request, product_id):
    w=Wishlist()
    w.user=request.user
    w.product=get_object_or_404(Product,id=product_id)
    w.save()
    
    products_id=Wishlist.objects.filter(user=request.user)
    products=Product.objects.filter(id__in=[item.product.id for item in products_id])
    return render(request, 'wishlist/wishlist.html', {'products': products})

def remove_from_wishlist(request, product_id):
    Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
    
    products_id=Wishlist.objects.filter(user=request.user)
    products=Product.objects.filter(id__in=[item.product.id for item in products_id])
    return render(request, 'wishlist/wishlist.html', {'products': products})

def wishlist_view(request):
    
    products_id=Wishlist.objects.filter(user=request.user)
    products=Product.objects.filter(id__in=[item.product.id for item in products_id])
    
    return render(request, 'wishlist/wishlist.html', {'products': products})