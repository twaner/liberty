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
    #is_business = request.POST.get('is_business')
    business = boolean_helper(request.POST.get('is_business'))
    client = Client(first_name=first_name, last_name=last_name, client_number=client_number,
                    business_name=business_name, is_business=business, address=args[0], contact_info=args[1])
    client.save()


def update_client(request, client, address, contact):
    """
    Updates a client object
    @param request: request from form
    @param client: Client to be updated
    @param address: Updated Address
    @param contact: Updated Contact
    @return: Updated Client
    """
    client.first_name = request.POST.get('first_name')
    client.last_name = request.POST.get('last_name')
    client.client_number = request.POST.get('client_number')
    client.business_name = request.POST.get('business_name')
    client.address = address
    client.contact_info = contact
    business = boolean_helper(request.POST.get('is_business'))
    client.is_business = business
    client.save(update_fields=['first_name', 'last_name', 'client_number', 'business_name', 'is_business',
                               'address', 'contact_info'])
    return client


def create_sales_prospect(request, *args):
    """
    creates a Sales_Prospect object from form
    @param request: request from form
    @param args: Contact object, Address object
    """
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


def update_sales_prospect(request, sales_prospect, address, contact):
    sales_prospect.first_name = request.POST.get('first_name')
    sales_prospect.last_name = request.POST.get('last_name')
    #sales_prospect.liberty_contact = request.POST.get('liberty_contact')
    sales_prospect.liberty_contact = Employee.objects.get(pk=request.POST.get('liberty_contact'))
    sales_prospect.sale_type = request.POST.get('sale_type')
    sales_prospect.probability = request.POST.get('probability')
    sales_prospect.initial_contact_date = request.POST.get('initial_contact_date')
    sales_prospect.comments = request.POST.get('comments')
    sales_prospect.address = address
    sales_prospect.contact_info = contact
    sales_prospect.save(update_fields=['first_name', 'last_name', 'liberty_contact', 'sale_type',
        'probability', 'initial_contact_date', 'comments', 'address', 'contact_info'])