"""CSFA2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from pages.views import * 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home_view,name='home'),
    path('',home_view,name='home'),
    path('ad/',admin_view,name='admin'),
    path('ad/tablestatus',table_stat_view,name='tablestatus'),
    path('ad/allbills',all_bill_view,name='allbills'),
    path('ad/changemenu',change_menu_view,name='changemenu'),
    path('customer/',customer_view,name='customer'),
    path('customer/menu/',menu_view,name='menu'),
    path('customer/menu/order/',order_view,name='order'),
    path('customer/bill/',bill1_view,name='bill1'),
    path('customer/bill/billresult/',b1_view,name='billresult'),
    path('customer/table',table_view,name='table'),
    
    
]
