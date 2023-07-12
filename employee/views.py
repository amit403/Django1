from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee


def employee(request):
    template = loader.get_template('frist.html')
    return HttpResponse(template.render())


def all_employee(request):
    allemp = Employee.objects.all().values()
    template = loader.get_template('All_employee.html')
    context = {
        "myemployee": allemp,
    }
    return HttpResponse(template.render(context, request))


def details(request,name):
    emp = Employee.objects.get(first_name=name)

    template = loader.get_template('details.html')
    context = {
        "selfemployee": emp,
    }
    return HttpResponse(template.render(context, request))

def home(request):

    template = loader.get_template('home.html')
    return HttpResponse(template.render())