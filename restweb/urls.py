"""
URL configuration for restweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authsys import views as authsys_views
from home import views as home_views
from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',authsys_views.signin,name='signin'),
    path('login/',authsys_views.login,name='login'),
    path('logout/',authsys_views.logout,name='logout'),
    path('delete_accout/',authsys_views.delete_account,name='delete_account'),
    path('home/',home_views.home,name='home'),
    path('admin_login/',authsys_views.admin_login,name='admin_login'),
    path('dashboard/',dashboard_views.dashboard,name='dashboard'),
    path('delete/<int:id>/',dashboard_views.delete_food,name='delete_food'),
    path('update/<int:id>/',dashboard_views.update_food,name='update_food'),
    path('add_food/',dashboard_views.add_food,name='add_food')

]
