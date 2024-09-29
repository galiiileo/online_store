# Generated by Django 5.1.1 on 2024-09-28 22:38

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('desc', models.TextField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, db_column='SKU', max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
                ('reviews_count', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('modified_at', models.DateField(blank=True, null=True)),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.productcategory')),
                ('inventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.productinventory')),
            ],
        ),
    ]
