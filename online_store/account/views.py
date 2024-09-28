from django.shortcuts import render

# Create your views here.
# views.py

from .forms import UserSignupForm  # Assuming you have a form for user signup

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserSignupForm, UserAddressForm, UserPaymentForm

def signup(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST, request.FILES)
        address_form = UserAddressForm(request.POST)
        payment_form = UserPaymentForm(request.POST)

        if user_form.is_valid() and address_form.is_valid() and payment_form.is_valid():
            user = user_form.save(commit=False)  # Don't save to DB yet
            user.password = user_form.cleaned_data['password']  # Get the plain password
            user.save()  # Now save the user

            # Save user address
            address = address_form.save(commit=False)
            address.user = user  # Associate the address with the user
            address.save()

            # Save user payment
            payment = payment_form.save(commit=False)
            payment.user = user  # Associate the payment with the user
            payment.save()

            messages.success(request, 'You have signed up successfully.')
            return redirect('login')  # Redirect to the login page

    else:
        user_form = UserSignupForm()
        address_form = UserAddressForm()
        payment_form = UserPaymentForm()

    return render(request, 'account/signup.html', {
        'user_form': user_form,
        'address_form': address_form,
        'payment_form': payment_form,
    })



from django.contrib.auth.hashers import check_password

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):  # Verify the hashed password
                request.session['user_id'] = user.id
                
               
                if user.role == 'admin':
                    return redirect('index')
                else:
                    return redirect('home_page')
            else:
                messages.error(request, 'Invalid password.')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')

    return render(request, 'account/login.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User
from .forms import UserUpdateForm

def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=user)  # Move this inside the else clause

    return render(request, "registration/profile.html", {'user': user, 'form': form})


