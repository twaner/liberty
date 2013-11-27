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


def update_employee(request, employee, address, contact):
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.employee_number = request.POST.get('employee_number')
        employee.hire_date = request.POST.get('hire_date')
        employee.pay_type = request.POST.get('pay_type')
        employee.pay_rate = request.POST.get('pay_rate')
        employee.address = address.id
        employee.contact_info = contact.id
        employee.termination_date = request.POST.get('termination_date')
        employee.termination_reason = request.POST.get('termination_reason')
        #handle title
        # all current titles
        title_list = request.POST.getlist('e_title')
        et_list = []
        [et_list.append(t) for t in employee.e_title.all()]
        # add titles
        for t in title_list:
            if t not in et_list:
                # new
                employee.e_title.add(t)
        # remove
        # e.e_title.filter(title_id=1).delete()
        for t in et_list:
            if t not in title_list:
                employee.e_title.filter(pk=int(t)).delete()
        """
        #update
        employee.save(update_fields['first_name', 'last_name', 'employee_number', ])
        contact.save(udpate_fields['phone', 'cell', 'email'])
        """


