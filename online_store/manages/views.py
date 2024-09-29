from itertools import product
from django.shortcuts import redirect
from django.shortcuts import render
from home.models import Product
from .forms import *
from order.models import OrderDetails
from order.models import OrderItems
from django.contrib.auth.decorators import user_passes_test
def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

# Create your views here.
@superuser_required
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
        return redirect('manage_products')
def edit_product(request,product_id):
    product = Product.objects.get(id=product_id)

    if request.method == "GET":

        form=ProductForm(instance=product)
        return render(request, "manages/productForm.html", context={"form":form})
    elif request.method == "POST":
        form=ProductForm(request.POST,request.FILES,instance=product)
        form.save()
        return redirect('manage_products')


def delete_product(request, product_id):
    Product.objects.get(id=product_id).delete()
    return redirect('manage_products')
def orders(request):
    orders=OrderDetails.objects.all()
    return render(request,"manages/manageOrders.html",{'orders':orders})
def edit_order(request,order_id):
    order = OrderDetails.objects.get(id=order_id)
    if request.method == "GET":
        form=OrderDetailsForm(instance=order)
        return render(request, "manages/orderForm.html", context={"form":form})
    elif request.method == "POST":
        form=OrderDetailsForm(request.POST,request.FILES,instance=order)
        form.save()
        return redirect('orders')