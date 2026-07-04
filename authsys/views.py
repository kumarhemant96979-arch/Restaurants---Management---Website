from django.shortcuts import render,redirect
from authsys.models import *
from .decorator import *
# Create your views here.

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('emial')

        User.objects.create(username=username,password=password,email=email)
        return redirect('login')
    
    return render(request,'signup_page.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('emial')

        user=User.objects.filter(username=username,password=password,email=email).first()

        if user:
            request.session['user_id']=user.id
        return redirect('home')
    
    return render(request,'login_page.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def delete_account(request):
    user_id=request.session.get('user_id')
    user=User.session.get(id=user_id)
    request.session.flush()
    user.delete()
    return redirect('signin')




