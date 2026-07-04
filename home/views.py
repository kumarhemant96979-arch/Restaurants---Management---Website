from django.shortcuts import render,redirect
from authsys.models import *
from authsys.decorator import *
# Create your views here.

@login_required_custom2
def home(request):
    user_id=request.session.get('user_id')
    user=User.objects.get(id=user_id)

    return render(request,'home_page.html',context={'user':user})

