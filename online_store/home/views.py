from django.shortcuts import render
from .models import Product, ProductCategory
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404


def home(request):
    products = Product.objects.all() [:4]
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, "home_page.html", context)

def all(request):
    products = Product.objects.all()
   
    return render(request, "all_products.html",{'products': products})


def search_results(request):
    search = request.GET.get('search', '')
    products = Product.objects.filter(name__startswith=search[:4])
    return render(request, 'search.html', {'products': products, 'search': search})

def category_view(request, category_id):
    category = get_object_or_404(ProductCategory, id=category_id)
    products = Product.objects.filter(category=category) 
    return render(request, 'category_view.html', {'category': category, 'products': products})


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")