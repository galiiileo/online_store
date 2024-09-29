from django.db import models

class CartItem(models.Model):
    user = models.ForeignKey('accounts.User', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)  




# class ShoppingSession(models.Model):
#     user = models.ForeignKey('accounts.User', models.DO_NOTHING, blank=True, null=True)
#     total = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
#     created_at = models.TextField(blank=True, null=True)  # This field type is a guess.



