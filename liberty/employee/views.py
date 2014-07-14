from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from employee.models import Employee, Title
from employee.forms import EmployeeForm, AddEmployeeForm
from common.models import Address, Contact, City
from common.forms import AddressForm, EmployeeContactForm, AddressFormPlaces, CityFormNotAuto
from helpermethods import create_employee, update_employee
from common.helpermethods import city_worker, create_address, create_employee_contact, handle_auto_city, update_address, update_employee_contact, validation_helper, form_generator, dict_generator


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
    context = {
        'employee_detail': employee_detail, 'address_detail': address_detail,
        'contact_detail': contact_detail, 'title_details': title_details
    }
    return render(request, 'employee/detail.html', context)


def empform(request):
    """
    Creates a new Employee.
    @param request: request.
    @return: redirect to index or form with validation errors.
    """
    form_list = form_generator(4)
    if request.method == 'POST':  # If form has been submitted...
        form_list[0] = AddEmployeeForm(request.POST)
        form_list[1] = CityFormNotAuto(request.POST)
        form_list[2] = AddressFormPlaces(request.POST)
        form_list[3] = EmployeeContactForm(request.POST)
        #form_list = [form0, form1, form2, form3]
        validation = validation_helper(form_list)

        if validation:
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
        form_list[0] = AddEmployeeForm()
        form_list[1] = CityFormNotAuto()
        form_list[2] = AddressFormPlaces()
        form_list[3] = EmployeeContactForm()
    form_dict = dict_generator(form_list)

    return render(request, 'title.html', form_dict)


def editemployee(request, employee_id):
    # bound form
    """
    Edits an Employee object
    @param request: request.
    @param employee_id: Employee pk.
    @return: redirect or form with validation errors.
    """
    form_list = form_generator(4)
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
    # form submission
    if request.method == 'POST':
        form_list[0] = EmployeeForm(request.POST)
        form_list[1] = CityFormNotAuto(request.POST)
        form_list[2] = AddressFormPlaces(request.POST)
        form_list[3] = EmployeeContactForm(request.POST)
        validation = validation_helper(form_list)

        if validation:
                cit = city_worker(request, request.POST.get('city_name'))
                address = update_address(request, address, cit)
                con = update_employee_contact(request, contact)
                employee = update_employee(request, employee, address, con)
                return HttpResponseRedirect('/employeetest/index/')
    else:
        # redisplay bound form
        form_list[0] = EmployeeForm(employee_dict)
        form_list[2] = AddressFormPlaces(address_dict)
        form_list[1] = CityFormNotAuto(city_dict)
        form_list[3] = EmployeeContactForm(contact_dict)
    form_dict = dict_generator(form_list)
    return render(request, 'employee/editemployee.html', form_dict)


def titleform(request):
    """
    Form to create employee.
    @param request: request.
    @return: rendered view or new employee and redirect.
    """
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


