from django.shortcuts import render
from home.models import Product
products=set([])
def add_to_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    products.add(product)
    return render(request, 'wishlist/wishlist.html', {'products': products})

def remove_from_wishlist(request, product_id):
    product = Product.objects.get(id=product_id)
    products.remove(product)
    return render(request, 'wishlist/wishlist.html', {'products': products})

def wishlist_view(request):
    return render(request, 'wishlist/wishlist.html')