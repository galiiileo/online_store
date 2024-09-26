from itertools import product
from django.shortcuts import redirect
from django.shortcuts import render
from home.models import Product
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'manages/index.html')
def manage_products(request):
    products = Product.objects.all()
    return render(request,"manages/manageProducts.html",{'products':products})
def add_product(request):
    if request.method == "GET":
        form=ProductForm()
        return render(request, 'manages/productForm.html', context={"form":form})
    elif request.method == "POST":
        form=ProductForm(request.POST, request.FILES)
        form.save()
        return redirect('home_page')
def edit_product(request,product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "GET":

        form=ProductForm(instance=product)
        return render(request, "manages/productForm.html", context={"form":form})
    elif request.method == "POST":
        form=ProductForm(request.POST,request.FILES,instance=product)
        form.save()
        return redirect('home_page')


def delete_product(request, product_id):
    Product.objects.get(id=product_id).delete()
    return redirect('home_page')