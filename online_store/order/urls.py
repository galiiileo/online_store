from django.urls import path
from .views import *

urlpatterns = [
    path("order_form", order_form, name='order_form'),
    path("order", order_form_view, name='order_form_view'),
]