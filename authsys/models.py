from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

class Admin(models.Model):
    admin_name=models.CharField(max_length=100)
    admin_key=models.CharField(max_length=100)
    admin_email=models.EmailField(unique=True)