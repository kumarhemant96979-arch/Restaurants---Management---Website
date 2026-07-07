from django.db import models
from authsys.models import *
# Create your models here.

class Food(models.Model):
    food_name=models.CharField(max_length=100)
    description=models.TextField(default="Delicious")
    image=models.ImageField(upload_to="foods/")
    price=models.IntegerField(default=1)
    is_available=models.BooleanField(default=True)
    category=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)