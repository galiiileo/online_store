
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from django.shortcuts import render, redirect
from .models import OrderDetails, OrderItems, PaymentDetails
from home.models import Product  # Assuming you have a Product model in home app
from django.utils import timezone



def order_form(request):
    products_id=CartItem.objects.filter(user=request.user)
    products=Product.objects.filter(id__in=[item.product.id for item in products_id])

    return render(request, 'order/order_form.html', {'products': products})
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from django.shortcuts import render, redirect
from .models import OrderDetails, OrderItems, PaymentDetails
from home.models import Product
from django.utils import timezone
from decimal import Decimal

@login_required
def order_form_view(request):
    user = request.user
    if request.method == 'POST':
        total_amount = request.POST.get('total_amount')
        payment_type = request.POST.get('payment_type')
        provider = request.POST.get('provider')
        account_no = request.POST.get('account_no')

        # Create PaymentDetails instance
        payment_details = PaymentDetails(
            provider=provider,
            amount=int(total_amount),
            status="pending",  # Set a default status, this can be changed later
            created_at=timezone.now(),
            modified_at=timezone.now()
        )
        payment_details.save()

        # Create OrderDetails instance
        order = OrderDetails(
            user=user,
            total=Decimal(total_amount),  # Use Decimal instead of int
            payment=payment_details,
            created_at=timezone.now(),
            modified_at=timezone.now(),
            status="pending"  # You can define other statuses like 'processed', 'shipped', etc.
        )
        order.save()

        # Handle OrderItems (for each product in the form)
        products = request.POST.getlist('product_2_name')  # Correct name of form field
        quantities = request.POST.getlist('product_2_quantity')  # Correct name of form field

        for product_name, quantity in zip(products, quantities):
            try:
                product = Product.objects.get(name=product_name)  # Fetch product by name
                order_item = OrderItems(
                    order=order,
                    product=product,
                    created_at=timezone.now(),
                    modified_at=timezone.now()
                )
                order_item.save()
            except Product.DoesNotExist:
                # Handle case where product is not found
                pass

        # Redirect or render a success message after saving the order
        return redirect('home_page')  # Assuming you have an order success page

    # If GET request, render the form with products from the cart
    products_id = CartItem.objects.filter(user=request.user)
    products = Product.objects.filter(id__in=[item.product.id for item in products_id])
    return render(request, 'order/order_form.html', {'products': products})
