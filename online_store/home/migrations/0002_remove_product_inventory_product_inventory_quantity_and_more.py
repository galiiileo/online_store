# Generated by Django 5.1.1 on 2024-09-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='inventory',
        ),
        migrations.AddField(
            model_name='product',
            name='inventory_quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ProductInventory',
        ),
    ]
