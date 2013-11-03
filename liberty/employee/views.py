from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from employee.models import Employee, Title, EmployeeForm, TitleForm
from common.models import Address, Contact, AddressForm, ContactForm


def tester(request):
    return HttpResponse("Test view working!")


def testconnection(request, employee_id):
    return HttpResponse("Employee id is %s" % employee_id)

# Workers =>
def bettertest(request):
    all_employees_list = Employee.objects.order_by('-employee_id')
    output = ', '.join([e.first_name for e in all_employees_list])
    return HttpResponse(output)


def indexer(request):
    all_employees_list = Employee.objects.order_by('-employee_id')
    context = {'all_employees_list': all_employees_list}
    return render(request, 'employee/indexer.html', context)


def detaileder(request, employee_id):
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

# FORMS
def index(request):
    return render(request, "employee/index.html")

def testing(request):
    return render(request, 'employee/test.html')

def search_form(request):
    return render(request, 'employee/search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        employees = Employee.objects.filter(first_name__icontains=q)
        return render(request, 'employee/search_results.html',
                      {'employees': employees, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def addemployee(request):
    return render(request, 'employee/addemployee.html')

"""
def employeeform(request):
    if request.method == 'POST': # If form has been submitted
        form = EmployeeForm(request.POST) # A form bound to POST data
        if form.is_valid():
            #process clean data
            return HttpResponseRedirect('/thanks/')
        else:
            form = EmployeeForm() # unbound form

    return render(request, 'addemployee.html', {
        'form': form
        })
"""
def titleform(request):
    form = TitleForm()

    return render(request, 'title.html', {'form': form})

def empform(request):
    form = EmployeeForm()
    form1 = AddressForm()

    return render(request, 'employee/empform.html', {'form': form, 'form1': form1})