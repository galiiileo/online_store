from django import forms
from home.models import Product
from order.models import OrderDetails

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields= ['status']