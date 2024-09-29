from django.urls import path
from .views import add_to_wishlist,remove_from_wishlist, wishlist_view

urlpatterns = [
    path('wishlist_add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist_remove/<int:product_id>/',remove_from_wishlist , name='remove_from_wishlist'),
    path('', wishlist_view, name='wishlist_view'),
        
]