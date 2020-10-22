from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Employee

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})

def employee_details(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee Doesn\'t Exist')
    return render(request, 'employee_details.html', {'employee': employee})