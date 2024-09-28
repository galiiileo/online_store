from django.shortcuts import render
from .models import CartItem, ShoppingSession
from home.models import Product

def cart_view(request):

    session = ShoppingSession.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(session=session)
    products = Product.objects.filter(id__in=cart_items.values('product_id'))


   
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'products': products})
