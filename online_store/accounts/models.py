from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    country=models.CharField(null=True,max_length=100)
    image=models.ImageField(upload_to='user_images',null=True)
    bio=models.TextField(null=True)
