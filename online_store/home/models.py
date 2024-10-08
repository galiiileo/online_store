from django.db import models
from datetime import date
from django.utils.timezone import now

class Product(models.Model): 
    name = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    sku = models.CharField(db_column='SKU', blank=True, null=True, max_length=255) 
    category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    inventory_quantity = models.IntegerField(blank=True, null=True)  # New field for inventory quantity
    price = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    reviews_count = models.CharField(blank=True, null=True, max_length=255)
    created_at = models.DateField(default=now)
    modified_at = models.DateField(blank=True, null=True)  
    deleted_at = models.DateField(blank=True, null=True) 




class ProductCategory(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    created_at = models.DateField(default=now)
    modified_at = models.DateField(blank=True, null=True)  
    deleted_at = models.DateField(blank=True, null=True)  






