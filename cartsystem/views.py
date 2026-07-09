from django.shortcuts import render,redirect
from authsys.views import *
from dashboard.views import *
from authsys.decorator import *
from cartsystem.models import *
# Create your views here.

def cart(request,id):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)
    food=Food.objects.get(id=id)

    cart_item=Cart.objects.filter(user=user,food=food,quantity=1).first()

    if cart_item:
        cart_item.quantity +=1
        cart_item.save()

    else:
        Cart.objects.create(user=user,food=food,quantity=1)

    cart_items=Cart.objects.filter(user=user)

    return render(request,'cart.html',context={'user':user,'cart_items':cart_items})





    

