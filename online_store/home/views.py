from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.filter(deleted_at__isnull=True)  # Adjust according to your logic
    return render(request, "home/home_page.html", {'products': products})