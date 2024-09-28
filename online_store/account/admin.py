from django.contrib import admin
from .models import User, UserAddress, UserPayment
from django.contrib.auth.hashers import make_password


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'telephone')
    list_filter = ('role',)
    search_fields = ('username', 'first_name', 'last_name')

    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'password', 'image', 'address', 'telephone', 'role')  # Include role
        }),
    )

def save_model(self, request, obj, form, change):
        if not change:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)




class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_line1', 'city', 'postal_code', 'country')
    search_fields = ('user__username', 'city', 'postal_code')
    list_filter = ('country',)

class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_type', 'provider', 'account_no')
    search_fields = ('user__username', 'payment_type', 'provider')


admin.site.register(User, UserAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserPayment, UserPaymentAdmin)
