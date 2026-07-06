from django.shortcuts import render,redirect
from authsys.models import *
from .decorator import *
# Create your views here.

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')

        User.objects.create(username=username,password=password,email=email)
        return redirect('login')
    
    return render(request,'signin_page.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')

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

def admin_login(request):
    if request.method=='POST':
        admin_name=request.POST.get("admin_name")
        admin_key=request.POST.get("admin_key")
        admin_email=request.POST.get("admin_email")

        admin=Admin.objects.filter(admin_name=admin_name,admin_key=admin_key,admin_email=admin_email).first()

        if admin:
            request.session['admin_id']=admin.id
        return redirect('dashboard')
    
    return render(request,'admin_login.html')





