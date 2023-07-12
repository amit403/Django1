from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("employee/",views.employee,name = "employee"),
    path("all_employee/details/<name>",views.details,name = "details"),
    path("all_employee/",views.all_employee,name = "all_employee"),
]