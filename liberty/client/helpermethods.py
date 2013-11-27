from models import Client, Sales_Prospect
from common.helpermethods import boolean_helper
from employee.models import Employee

def create_client(request, *args):
    #client
    """
    Takes a request, Address, and City and creates a new client
    @param request:
    @param args: Address, City
    """
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    client_number = request.POST.get('client_number')
    business_name = request.POST.get('business_name')
    is_business = request.POST.get('is_business')
    print("BUS", is_business)
    # is business
    business = boolean_helper(is_business)
    """
    print('before if is business', is_business)
    if is_business == 'None':
        business = False
        print('is bus == none', is_business)
    elif is_business == 'on':
        print('is business == on', is_business)
        business = True
    """
    print('after', business)
    client = Client(first_name=first_name, last_name=last_name, client_number=client_number,
                    business_name=business_name, is_business=business, address=args[0], contact_info=args[1])
    client.save()


def create_sales_prospect(request, *args):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    # handle no liberty contact
    #if liberty_contact = request.POST.get('liberty_contact') != ''
    try:
        liberty_contact = Employee.objects.get(pk=request.POST.get('liberty_contact'))
    except ValueError:
        liberty_contact = None
    sale_type = request.POST.get('sale_type')
    probability = request.POST.get('probability')
    initial_contact_date = request.POST.get('initial_contact_date')
    comments = request.POST.get('comments')
    is_client = False
    #handle is client --> address=None, contact_info=None
    #client = boolean_helper(is_client)
    if len(args) == 1:
        address = None
    else:
        address = args[1]
    sales = Sales_Prospect(first_name=first_name, last_name=last_name, liberty_contact=liberty_contact,
                           sale_type=sale_type, probability=probability, initial_contact_date=initial_contact_date,
                           comments=comments, address=address, contact_info=args[0], is_client=is_client)
    sales.save()
