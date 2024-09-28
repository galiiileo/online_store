from django.db import models


class OrderDetails(models.Model):
    user = models.ForeignKey('account.User', models.DO_NOTHING, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    payment = models.ForeignKey('PaymentDetails', models.DO_NOTHING, blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    modified_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_details'


class OrderItems(models.Model):
    order = models.ForeignKey(OrderDetails, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey("home.Product", models.DO_NOTHING, blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    modified_at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'order_items'


class PaymentDetails(models.Model):
    order = models.ForeignKey(OrderDetails, models.DO_NOTHING, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    provider = models.CharField(blank=True, null=True, max_length=255)
    status = models.CharField(blank=True, null=True, max_length=255)
    created_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    modified_at = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'payment_details'
