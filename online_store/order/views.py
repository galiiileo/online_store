from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from home.models import Product

# Create your views here.
def order_form(request):
    products_id=CartItem.objects.filter(user=request.user)
    products=Product.objects.filter(id__in=[item.product.id for item in products_id])
    
    return render(request, 'order/order_form.html', {'products': products})



@login_required
def order_form_view(request):
    user = request.user

    initial_data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "telephone": user.profile.phone if hasattr(user, 'profile') else '',  
        "address_line1": user.profile.address_line1 if hasattr(user, 'profile') else '',
        "address_line2": user.profile.address_line2 if hasattr(user, 'profile') else '',
        "city": user.profile.city if hasattr(user, 'profile') else '',
        "postal_code": user.profile.postal_code if hasattr(user, 'profile') else '',
        "country": user.profile.country if hasattr(user, 'profile') else '',
        "provider": user.profile.payment_provider if hasattr(user, 'profile') else '',
        "account_no": user.profile.account_no if hasattr(user, 'profile') else '',

        "product_name": user.profile.product_name if hasattr(user, 'profile') else '',  
        "total_amount": user.profile.total_amount if hasattr(user, 'profile') else '',
    }

    return render(request, 'order/order_form.html', {'initial_data': initial_data})