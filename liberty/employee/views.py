from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from employee.models import Employee, Title
from employee.forms import EmployeeForm, TitleForm, AddEmployeeForm
from common.models import Address, Contact, City
from common.forms import AddressForm, EmployeeContactForm, CityForm


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


def titleform1(request):
    print("title view called")
    if request.method == 'POST':
        print("POST called")
        form = TitleForm()
    else:
        print('ELSE CALLED')
        form = TitleForm()
    return render(request, 'title.html', {'form': form})


def empform(request):
    print("empform long view called")
    if request.method == 'POST':  # If form has been submitted...
        print("POST ==")
        form = AddEmployeeForm(request.POST)
        form1 = AddressForm(request.POST)
        form2 = EmployeeContactForm(request.POST)
        #form3 = CityForm(request.POST)
        f_valid = form.is_valid()
        f1_valid = form1.is_valid()
        f2_valid = form2.is_valid()
        #debugging
        print("Form validation: ", f_valid, "1:", f1_valid, "2:", f2_valid)
        print(request.POST.get('pay_type'))
        print(request.POST.get('city-autocomplete'))
        print(request.POST.get('city'))

        if form.is_valid() and form1.is_valid() and form2.is_valid():
            # city name from form
            city_n = request.POST.get('city')

            #print(City.objects.get(city_n))
            print(type(city_n))

            # check to see if that city is in db i.e. count > 1
            #city = City.objects.filter(city_name__icontains=city_n).count()
            # if exists get object from db else create new city object and save.
            c = City
            if city_n > 1:
                # assign value to City variable
                c = City.objects.get(pk=city_n)
                #c = City.objects.get(city_name__icontains=city_n)
            else:
                # save new city
                c = City(city_name=city_n)
                c.save()
            # address
            print(c.city_name)

            address = request.POST.get('address')
            address2 = request.POST.get('address2')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip_code')
            a = Address(address=address, address2=address2, city=c, state=state,
                        zip_code=zip_code)
            a.save()

            # contact
            phone = request.POST.get('phone')
            cell = request.POST.get('cell')
            email = request.POST.get('email')
            con = Contact(phone=phone, cell=cell, email=email)
            con.save()

            # employee
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            employee_number = request.POST.get('employee_number')
            hire_date = request.POST.get('hire_date')
            pay_type = request.POST.get('pay_type')
            pay_rate = request.POST.get('pay_rate')
            e = Employee(first_name=first_name, last_name=last_name, employee_number=employee_number,
                         address=a, contact_info=con, hire_date=hire_date, pay_type=pay_type,
                         pay_rate=pay_rate)
            e.save()
            # handle m2m field
            [e.e_title.add(et) for et in request.POST.getlist('e_title')]
            #e.save_m2m()

            return HttpResponseRedirect('/employeetest/index/')
    else:
        # unbound forms
        form = AddEmployeeForm()
        form1 = AddressForm()
        form2 = EmployeeContactForm()
        #form3 = CityForm()

    return render(request, 'title.html', {'form': form, 'form1': form1,
                                          'form2': form2})


""" """


def titleform(request):
    print("titleform view called")
    if request.method == 'POST':
        print("POST called")
        form = AddEmployeeForm()
        form1 = AddressForm(request.POST)
        form2 = EmployeeContactForm(request.POST)
    else:
        print('ELSE CALLED!!!')
        form = AddEmployeeForm()
        form1 = AddressForm()
        form2 = EmployeeContactForm()
    return render(request, 'title.html', {'form': form, 'form1': form1, 'form2': form2})


def empform1(request):
    print("empform1 view called")
    if request.method == 'POST': # If form has been submitted...
        print("POST ==")
        print("form constructors")
        form = AddEmployeeForm(request.POST)
        form1 = AddressForm(request.POST)
        form2 = EmployeeContactForm(request.POST)
    else:
        # unbound forms
        print("ELSE CALLED!!!")
        form = AddEmployeeForm()
        form1 = AddressForm()
        form2 = EmployeeContactForm()

    return render(request, 'employee/empform.html', {'form': form, 'form1': form1,
                                                     'form2': form2})