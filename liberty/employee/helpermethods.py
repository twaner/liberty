from models import Employee
from common.models import Address, Contact

def create_employee(request, *args):
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
        # handle m2m field
        [e.e_title.add(et) for et in request.POST.getlist('e_title')]

