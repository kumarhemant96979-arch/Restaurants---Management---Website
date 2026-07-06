from django.shortcuts import render
from authsys.models import *
from authsys.decorator import *
# Create your views here.

@login_required_custom2
def dashboard(request):
    admin_id=request.session.get('admin_id')
    admin=Admin.objects.get(id=admin_id)

    return render(request,'dashboard.html',context={'admin':admin})

