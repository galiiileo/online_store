
from django.contrib import admin
from .models import Product, ProductCategory, ProductInventory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'price', 'inventory', 'created_at')  # Fields to display in the admin list view
    search_fields = ('name', 'sku')  # Fields that can be searched
    list_filter = ('category', 'price')  # Filters to apply in the sidebar

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Fields to display in the admin list view
    search_fields = ('name',)  # Fields that can be searched

class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'created_at')  # Fields to display in the admin list view

# Register the models
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductInventory, ProductInventoryAdmin)
