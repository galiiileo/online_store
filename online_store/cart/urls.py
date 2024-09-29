from django.urls import path
from .views import add_to_cart,remove_from_cart, cart_view, clear_cart

urlpatterns = [
    path('cart_add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart_remove/<int:product_id>/',remove_from_cart , name='remove_from_cart'),
    path('clear_cart/',  clear_cart, name='clear_cart'),
    path('', cart_view, name='cart_view'),
        
]