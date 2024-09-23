from django.db import models
from datetime import date
from django.utils.timezone import now

class Product(models.Model): 
    name = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    sku = models.CharField(db_column='SKU', blank=True, null=True, max_length=255) 
    category = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    inventory = models.ForeignKey('ProductInventory', models.DO_NOTHING, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  
    created_at = models.DateField(default=now)
    modified_at = models.DateField(blank=True, null=True)  
    deleted_at = models.DateField(blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'product'

class ProductInventory(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(default=date.today)  
    modified_at = models.DateField(blank=True, null=True)  
    deleted_at = models.DateField(blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'product_inventory'


class ProductCategory(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    created_at = models.DateField(default=now)
    modified_at = models.DateField(blank=True, null=True)  
    deleted_at = models.DateField(blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'product_category'
