from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from employee.models import Employee, Title
from employee.forms import EmployeeForm, TitleForm, AddEmployeeForm
from common.models import Address, Contact, City
from common.forms import AddressForm, EmployeeContactForm, CityForm, AddressFormPlaces, CityFormNotAuto
from helpermethods import create_employee, update_employee
from common.helpermethods import city_worker, create_address, create_employee_contact, handle_auto_city, update_address,update_employee_contact


def index(request):
    """
    List of all Employees.
    @param request: request.
    @return: rendered view with all Employees.
    """
    all_employees_list = Employee.objects.order_by('last_name')
    context = {'all_employees_list': all_employees_list}
    return render(request, 'employee/index.html', context)


def details(request, employee_id):
    """
    Detailed view of Employee.
    @param request: request.
    @param employee_id: Employee pk.
    @return: rendered view with Employee details.
    """
    employee_detail = Employee.objects.get(pk=employee_id)
    address_detail = Address.objects.get(pk=employee_detail.address_id)
    contact_detail = Contact.objects.get(pk=employee_detail.contact_info_id)
    title_details = employee_detail.e_title.all()
    context = {'employee_detail': employee_detail, 'address_detail': address_detail,
               'contact_detail': contact_detail, 'title_details': title_details}
    return render(request, 'employee/detail.html', context)


def empform(request):
    """
    Creates a new Employee.
    @param request: request.
    @return: redirect to index or form with validation errors.
    """
    print("EMPFORM LONG VIEW CALLED")
    if request.method == 'POST':  # If form has been submitted...
        print("POST ==")
        form = AddEmployeeForm(request.POST)
        form1 = CityFormNotAuto(request.POST)
        form2 = AddressFormPlaces(request.POST)
        form3 = EmployeeContactForm(request.POST)

        f_valid = form.is_valid()
        f1_valid = form1.is_valid()
        f2_valid = form2.is_valid()
        f3_valid = form3.is_valid()

        if f_valid and f1_valid and f2_valid and f3_valid:
            #city
            city_f = request.POST.get('city_name')
            c = city_worker(request, city_f)
            # address
            a = create_address(request, c)
            # contact
            con = create_employee_contact(request)
            # employee
            e = create_employee(request, a, con)

            return HttpResponseRedirect('/employeetest/index/')
    else:
        # unbound forms
        form = AddEmployeeForm()
        form1 = CityFormNotAuto()
        form2 = AddressFormPlaces()
        form3 = EmployeeContactForm()

    return render(request, 'title.html', {'form': form, 'form1': form1,
                                          'form2': form2, 'form3': form3})


def editemployee(request, employee_id):
    # bound form
    """
    Edits an Employee object
    @param request: request.
    @param employee_id: Employee pk.
    @return: redirect or form with validation errors.
    """
    employee = Employee.objects.get(pk=employee_id)
    address = Address.objects.get(pk=employee.address_id)
    contact = Contact.objects.get(pk=employee.contact_info_id)
    city = City.objects.get(pk=address.city_id)
    title_details = employee.e_title.all()
    # create data dictionaries
    employee_dict = {'first_name': employee.first_name, 'last_name': employee.last_name,
                'employee_number': employee.employee_number, 'e_title': title_details,
                'hire_date': employee.hire_date, 'pay_type': employee.pay_type,
                'pay_rate': employee.pay_rate, 'termination_date': employee.termination_date,
                'termination_reason': employee.termination_reason
    }
    address_dict = {'address': address.address, 'address2': address.address2,
                    'city': address.city_id, 'state': address.state, 'zip_code': address.zip_code
    }
    contact_dict = {'phone': contact.phone, 'cell': contact.cell, 'email': contact.email}
    city_dict = {'city_name': city.city_name}

    form = EmployeeForm(request.POST)
    form2 = AddressFormPlaces(request.POST)
    form3 = EmployeeContactForm(request.POST)
    form1 = CityFormNotAuto(request.POST)

    # validation vars
    form_v = form.is_valid()
    form2_v = form2.is_valid()
    form3_v = form3.is_valid()
    form1_v = form1.is_valid()
    if form_v and form2_v and form3_v and form1_v:
            cit = city_worker(request, request.POST.get('city_name'))
            address = update_address(request, address, cit)
            con = update_employee_contact(request, contact)
            #sales prospect
            employee = update_employee(request, employee, address, con)
            return HttpResponseRedirect('/employeetest/index/')
    else:
        # redisplay bound form
        form = EmployeeForm(employee_dict)
        form2 = AddressFormPlaces(address_dict)
        form1 = CityFormNotAuto(city_dict)
        form3 = EmployeeContactForm(contact_dict)
    return render(request, 'employee/editemployee.html', {'form': form, 'form1': form1,
                                                          'form2': form2, 'form3': form3})


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


"""
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
            #e.save_m2m() """

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

def detaileder(request, employee_id):
    employee_detail = Employee.objects.get(pk=employee_id)
    context = {'employee_detail': employee_detail}
    return render(request, 'employee/detail.html', context)

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
def tester(request):
    return HttpResponse("Test view working!")


def testconnection(request, employee_id):
    return HttpResponse("Employee id is %s" % employee_id)

# Workers =>
def bettertest(request):
    all_employees_list = Employee.objects.order_by('-employee_id')
    output = ', '.join([e.first_name for e in all_employees_list])
    return HttpResponse(output)

def titleform1(request):
    print("title view called")
    if request.method == 'POST':
        print("POST called")
        form = TitleForm()
    else:
        print('ELSE CALLED')
        form = TitleForm()
    return render(request, 'title.html', {'form': form})

## original empform
def empform(request):

    print("EMPFORM LONG VIEW CALLED")
    if request.method == 'POST':  # If form has been submitted...
        print("POST ==")
        form = AddEmployeeForm(request.POST)
        form1 = AddressForm(request.POST)
        form2 = EmployeeContactForm(request.POST)
        f_valid = form.is_valid()
        f2_valid = form2.is_valid()

        # Handle autocomplete
        print("City auto / type", request.POST.get('city-autocomplete'), type(request.POST.get('city-autocomplete')))
        print("City", request.POST.get('city'), type(request.POST.get('city')))

        cc = handle_auto_city(request)
        if cc != "None":
            f1_valid = True
        else:
            f1_valid = False

        c = city_worker(request, cc)
        print("CITY WORKER: TYPE / ID", c, type(c), c.city_id)
        if form1.is_valid():
            form1.save(commit=False)
            form1.city = c.city_id
            print "FORM1 city, pk", form1.city
            form1.save()
        q = create_employee(request, c, form1)
        if not form1.is_valid():
            print form1.errors
        print "ADDRESSFORM VALID: ", form1.is_valid()

        #debugging
        print("Form validation: ", f_valid, "1:", f1_valid, "2:", f2_valid)
        print(request.POST.get('pay_type'))
        print("City auto / type", request.POST.get('city-autocomplete'), type(request.POST.get('city-autocomplete')))
        print("City", request.POST.get('city'), type(request.POST.get('city')))
        print("City from handle:", cc)

        if form.is_valid() and form1.is_valid() and form2.is_valid():
            #c = city_worker(request, cc)
            # address
            a = create_address(request, c)
            # contact
            con = create_employee_contact(request)
            #sales prospect
            e = create_employee(request, a, con)

            return HttpResponseRedirect('/employeetest/index/')
    else:
        # unbound forms
        form = AddEmployeeForm()
        form1 = AddressForm()
        form2 = EmployeeContactForm()
        #form3 = CityForm()

    return render(request, 'title.html', {'form': form, 'form1': form1,
                                          'form2': form2})


def empform2(request):
    print("empform1 view called")
    if request.method == 'POST':  # If form has been submitted...
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

def editemployee(request, employee_id):
    # bound form

    Edits an Employee object
    @param request: request.
    @param employee_id: Employee pk.
    @return: redirect or form with validation errors.

    e = Employee.objects.get(pk=employee_id)
    a = Address.objects.get(pk=e.address_id)
    c = Contact.objects.get(pk=e.contact_info_id)
    title_details = e.e_title.all()
    # create data dictionaries
    employee = {'first_name': e.first_name, 'last_name': e.last_name,
                'employee_number': e.employee_number, 'e_title': title_details,
                'hire_date': e.hire_date, 'pay_type': e.pay_type, 'pay_rate': e.pay_rate,
                'termination_date': e.termination_date, 'termination_reason': e.termination_reason
    }
    address = {'address': a.address, 'address2': a.address2, 'city': a.city_id,
               'state': a.state, 'zip_code': a.zip_code
    }
    contact = {'phone': c.phone, 'cell': c.cell, 'email': c.email}

    for k, v in address.iteritems():
        print("K ? V", k,v)

    if request.method == 'POST':
        f = EmployeeForm(request.POST)
        f1 = AddressForm(request.POST)
        f2 = EmployeeContactForm(request.POST)
        f_v = f.is_valid()
        f2_v = f2.is_valid()

        #city
        cc = handle_auto_city(request)
        if cc != "None":
            f1_valid = True
        else:
            f1_valid = False

        city_obj = city_worker(request, cc)

        if f_v and f2_v and f1_valid:
            # address
            a = update_address(request, a, city_obj)
            # contact
            con = update_employee_contact(request, c)
            #sales prospect
            e = update_employee(request, e, a, con)

        return HttpResponseRedirect('/employeetest/index/')
    else:
        # redisplay bound form
        form = EmployeeForm(employee)
        form1 = AddressForm(address)
        form2 = EmployeeContactForm(contact)
    return render(request, 'employee/editemployee.html', {'form': form, 'form1': form1,
                                                          'form2': form2})

"""