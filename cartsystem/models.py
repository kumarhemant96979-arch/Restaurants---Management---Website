from django.db import models
from authsys.models import *
from home .models import *
from dashboard.models import *
# Create your models here.

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    added_time=models.DateTimeField(auto_now_add=True)


