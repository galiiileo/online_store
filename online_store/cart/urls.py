from django.urls import path
from .views import cart_view

urlpatterns = [
    path('usercart/', cart_view, name='cart_view')
    
]