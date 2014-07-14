from models import Employee, Title
from common.models import Address, Contact

## EMPLOYEE HELPERS
def create_employee(request, *args):
    """
    Creates Employee object.
    @param request: request.
    @param args: Address and Contact.
    """
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    employee_number = request.POST.get('employee_number')
    hire_date = request.POST.get('hire_date')
    pay_type = request.POST.get('pay_type')
    pay_rate = request.POST.get('pay_rate')
    if type(args[0]) == Address:
        a = args[0]
        c = args[1]
    elif type(args[1]) == Address:
        a = args[1]
        c = args[0]

    e = Employee(first_name=first_name, last_name=last_name, employee_number=employee_number,
                 address=a, contact_info=c, hire_date=hire_date, pay_type=pay_type,
                 pay_rate=pay_rate)
    e.save()
    print("TYPE OF REQUEST.POST.getLIST ==>", type(request.POST.getlist('e_title')))
    # handle m2m field
    [e.e_title.add(et) for et in request.POST.getlist('e_title')]
    e.save()


def update_employee(request, employee, address, contact):
    """
    updates Employee object
    @param request: request from form
    @param employee: Employee Object to be updated
    @param address: Address object
    @param contact: Contact object
    @return: Updated Employee
    """
    employee.first_name = request.POST.get('first_name')
    employee.last_name = request.POST.get('last_name')
    employee.employee_number = request.POST.get('employee_number')
    employee.hire_date = request.POST.get('hire_date')
    employee.pay_type = request.POST.get('pay_type')
    employee.pay_rate = request.POST.get('pay_rate')
    employee.address = address
    employee.contact_info = contact
    employee.termination_date = request.POST.get('termination_date')
    employee.termination_reason = request.POST.get('termination_reason')
    print("TERMINATION DATE ", employee.termination_date, employee.termination_date == '')
    #handle title
    # all current titles.
    title_list = request.POST.getlist('e_title')
    # list of employee's previous titles.
    et_list = []
    [et_list.append(unicode(t.title_id)) for t in employee.e_title.all()]

    [employee.e_title.add(t) for t in title_list if t not in et_list]

    [employee.e_title.remove(t) for t in et_list if t not in title_list]
        #update
    employee.save(update_fields=['first_name', 'last_name', 'employee_number', 'hire_date',
                                 'pay_type', 'pay_rate', 'address', 'contact_info', 'termination_reason'])
    if employee.termination_date != '':
        employee.save(update_fields=['termination_date'])
    return employee

