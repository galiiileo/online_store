from django.db import models

class CartItem(models.Model):
    user = models.ForeignKey('accounts.User', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('home.Product', models.DO_NOTHING,blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)  
    
    def __str__(self):
        return f"{self.user} - {self.product}"








