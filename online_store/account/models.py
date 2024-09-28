from django.db import models
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    
    username = models.CharField(blank=True, null=True, max_length=255)
    password = models.CharField(blank=True, null=True, max_length=255)
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=255)
    telephone = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    created_at = models.DateField(default=now)
    modified_at = models.DateField(blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'user'


    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(blank=True, null=True,max_length=255)
    address_line2 = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True,max_length=255)
    postal_code = models.CharField(blank=True, null=True,max_length=255)
    country = models.CharField(blank=True, null=True,max_length=255)
    telephone = models.CharField(blank=True, null=True, max_length=255)
    mobile = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'user_address'


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(blank=True, null=True,max_length=255)
    provider = models.CharField(blank=True, null=True,max_length=255)
    account_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_payment'
