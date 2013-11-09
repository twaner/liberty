from models import Client, Sales_Prospect
from common.helpermethods import boolean_helper

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
    liberty_contact = request.POST('liberty_contact')
    sale_type = request.POST('sale_type')
    probability = request.POST('probability')
    initial_contact_date = request.POST('initial_contact_date')
    comments = request.POST('comments')
    is_client = request.POST('is_client')
    #handle is client
    client = boolean_helper(is_client)
    sales = Sales_Prospect(first_name=first_name, last_name=last_name,liberty_contact=liberty_contact,sale_type=sale_type,
                           probability=probability, initial_contact_date=initial_contact_date, comments=comments,
                           is_client=is_client, address=args[0], contact_info=args[1])
    sales.save()
