
from django import forms
from .models import User, UserAddress, UserPayment


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'first_name', 
            'last_name', 
            'image', 
            'address', 
            'telephone',
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = [
            'address_line1', 
            'address_line2', 
            'city', 
            'postal_code', 
            'country', 
            'telephone', 
            'mobile',
        ]


class UserPaymentForm(forms.ModelForm):
    class Meta:
        model = UserPayment
        fields = [
            'payment_type', 
            'provider', 
            'account_no', 
            
        ]




from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())

from .models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'address', 'telephone', 'image']
