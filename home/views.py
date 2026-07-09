from django.shortcuts import render,redirect
from authsys.models import *
from authsys.decorator import *
from dashboard.models import *
# Create your views here.

@login_required_custom2
def home(request):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    return render(request,'home_page.html',context={'user':user})

@login_required_custom2
def view_menu(request):
    user_id=request.session.get("user_id")
    user=User.objects.get(id=user_id)

    foods=Food.objects.all()

    return render(request,'view_menu.html',context={'foods':foods})

@login_required_custom2
def profile(request):
    user_id=request.session.get("user_id")
    user=User.objects.get(id=user_id)
    if request.method=="POST":
        phone_number=request.POST.get("phone_number")
        address=request.POST.get("address")

        user.phone_number=phone_number
        user.address=address
        print(request.POST)
        print(phone_number)
        print(address)
        user.save()

        return redirect('home')
   
    return render(request,'profile.html',context={'user':user})





