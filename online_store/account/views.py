from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserAddressForm, UserPaymentForm

def signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST, request.FILES)
        address_form = UserAddressForm(request.POST)
        payment_form = UserPaymentForm(request.POST)

        if user_form.is_valid() and address_form.is_valid() and payment_form.is_valid():
            user = user_form.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()

            payment = payment_form.save(commit=False)
            payment.user = user
            payment.save()

            return redirect('login')  # Redirect to a success page or dashboard

    else:
        user_form = UserSignupForm()
        address_form = UserAddressForm()
        payment_form = UserPaymentForm()

    context = {
        'user_form': user_form,
        'address_form': address_form,
        'payment_form': payment_form,
    }
    
    return render(request, 'account/signup.html', context)


# views.py
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserAddressForm, UserPaymentForm, UserLoginForm

# Existing signup view...

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('success')  # Redirect to a success page or dashboard
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = UserLoginForm()

    return render(request, 'account/login.html', {'form': form})


def profile(request):
    return render (request,"registration/profile.html")