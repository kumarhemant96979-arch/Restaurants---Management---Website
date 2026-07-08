from django.shortcuts import render
from authsys.models import *
from dashboard.models import *
from authsys.decorator import *
# Create your views here.

@login_required_custom2
def dashboard(request):
    admin_id=request.session.get('admin_id')
    admin=Admin.objects.get(id=admin_id)

    return render(request,'dashboard.html',context={'admin':admin})

def add_food(request):
    if request.method=="POST":
        food_name=request.POST.get("food_name")
        description=request.POST.get("description")
        image=request.FILES.get("image")
        price=request.POST.get("price")
        category=request.POST.get("category")

        Food.objects.create(food_name=food_name,description=description,image=image,price=price,category=category)
        return redirect('dashboard')
    
    foods=Food.objects.all()
    
    return render(request,'menu.html',context={'foods':foods})

def delete_food(request,id):
    food=Food.objects.get(id=id)
    food.delete()
    return redirect('add_food')

def update_food(request,id):
    food=Food.objects.get(id=id)
    if request.method=='POST':
        food_name=request.POST.get("food_name")
        description=request.POST.get("description")
        image=request.FILES.get("image")
        price=request.POST.get("price")
        category=request.POST.get("category")

        food.food_name=food_name
        food.description=description
        food.image=image
        if image:
            food.image=image
        food.price=price
        food.category=category

        food.save()
        return redirect('add_food')
    
    return render(request,'menu_update.html',context={'food':food})






