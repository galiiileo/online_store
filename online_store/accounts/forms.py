from django import forms
from django.contrib.auth.models import AbstractUser
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password','image','phone_number']
        widgets = {
            'password': forms.PasswordInput()
        }
