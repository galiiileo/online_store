# Generated by Django 5.1.1 on 2024-09-27 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpayment',
            name='expiry',
        ),
    ]
