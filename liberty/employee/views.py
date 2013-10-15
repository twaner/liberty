from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from employee.models import Employee, Title
from common.models import Address, Contact

def tester(request):
    return HttpResponse("Test view working!")

def testconnection(request, employee_id):
    return HttpResponse("Employee id is %s" % employee_id)

# Workers =>
def bettertest(request):
    all_employees_list = Employee.objects.order_by('-employee_id')
    output = ', '.join([e.first_name for e in all_employees_list])
    return HttpResponse(output)

def index(request):
    all_employees_list = Employee.objects.order_by('-employee_id')
    context = {'all_employees_list': all_employees_list}
    return render(request, 'employee/index.html', context)


def detailed(request, employee_id):
    employee_detail = Employee.objects.get(pk=employee_id)
    context = {'employee_detail': employee_detail}
    return render(request, 'employee/detail.html', context)

def detailed(request, employee_id):
    employee_detail = Employee.objects.get(pk=employee_id)
    address_detail = Address.objects.get(pk=employee_detail.address_id)
    contact_detail = Contact.objects.get(pk=employee_detail.contact_info_id)
    title_details = employee_detail.e_title.all()
    context = {'employee_detail': employee_detail, 'address_detail': address_detail,
               'contact_detail': contact_detail, 'title_details': title_details}
    return render(request, 'employee/detail.html', context)
