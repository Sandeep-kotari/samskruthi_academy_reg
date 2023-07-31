from django.contrib import admin
from django.urls import path
from admissionapp import views

urlpatterns = [
    path("",views.index,name="index"),
    path("form1",views.form1,name="form1"),
    path("form2",views.form2,name="form2"),
    path("form3",views.form3,name="form3"),
    path("gbill",views.gbill,name="gbill"),
    path("billgen", views.billgen,name="billgen"),
]
