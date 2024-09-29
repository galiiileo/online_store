from django.contrib import admin
from .models import Product, ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'inventory_quantity', 'created_at')
    search_fields = ('name', 'sku')
    list_filter = ('category', 'price')

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

# Register the models
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
