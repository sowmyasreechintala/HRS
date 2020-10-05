"""HRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

from adminapp import views

urlpatterns = [
   path('',views.showindex,name='main'),
   path('admin_login_check/',views.admin_login_check,name='admin_login_check'),
   path('welcome/',views.welcome,name='welcome'),
   path('admin_logout/',views.admin_logout,name="admin_logout"),
   path('admin_add_rooms/',views.admin_add_rooms,name="admin_add_rooms"),
   path('admin_save_room/',views.admin_save_room,name="admin_save_room"),
   path('admin_edit_rooms/',views.admin_edit_rooms,name='admin_edit_rooms'),
   path('editing_process/',views.editing_process,name="editing_process"),
   path('admin_reports/',views.admin_reports,name="admin_reports"),
   path('admin_search/',views.admin_search,name="admin_search"),
    path('admin_delete_room/',views.admin_delete_room, name="admin_delete_room"),
   path('admin_update_edit/',views.admin_update_edit,name="admin_update_edit")

]
