from django.db import models
from django.utils.timezone import now


class User(models.Model):
    username = models.CharField(blank=True, null=True, max_length=255)
    password = models.TextField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=255)
    telephone = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(default=now)
    modified_at = models.DateField(blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'user'


class UserAddress(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    address_line1 = models.CharField(blank=True, null=True, max_length=255)
    address_line2 = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True, max_length=255)
    postal_code = models.CharField(blank=True, null=True, max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)
    telephone = models.CharField(blank=True, null=True, max_length=255)
    mobile = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'user_address'


class UserPayment(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    payment_type = models.CharField(blank=True, null=True, max_length=255)
    provider = models.CharField(blank=True, null=True, max_length=255)
    account_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_payment'
