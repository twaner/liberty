from models import Address, City, Contact


def create_address(request, city):
    """
    Takes a request and builds and saves an Address
    @param request:
    @param city:
    @return: Address object
    """
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    state = request.POST.get('state')
    print("create_address:CITY", city)
    zip_code = request.POST.get('zip_code')
    a = Address(address=address, address2=address2, city=city, state=state,
                zip_code=zip_code)
    a.save()
    return a


def update_address(request, address, city):
    """
    Updates an Address object
    @param request: request data
    @param address: address object. validated in view
    @return: updated address
    """
    print "ADDRESS CITY UPDATE", type(address), city, type(city), city
    address.address = request.POST.get('address')
    address.address2 = request.POST.get('address2')
    address.state = request.POST.get('state')
    print("update_address:CITY", city)
    address.zip_code = request.POST.get('zip_code')
    address.city = city
    address.save(update_fields=['address', 'address2', 'city', 'state', 'zip_code'])
    return address

def create_contact(request):
    """
    Takes a request and returns a contact
    @param request:
    @return: Contact Object
    """
    phone = request.POST.get('phone')
    phone_extension = request.POST.get('phone_extension')
    cell = request.POST.get('cell')
    office = request.POST['office_phone']
    office_extension = request.POST['office_phone_extension']
    email = request.POST.get('email')
    website = request.POST.get('website')
    con = Contact(phone=phone, phone_extension=phone_extension, cell=cell, email=email,
                  office_phone=office, office_phone_extension=office_extension, website=website)
    con.save()
    return con


def update_contact(request, contact):
    """
    Updates a Contact object
    @param request: request from form
    @param contact: Contact object
    @return: updated Contact object
    """
    contact.phone = request.POST.get('phone')
    contact.phone_extension = request.POST.get('phone_extension')
    contact.cell = request.POST.get('cell')
    contact.office = request.POST['office_phone']
    contact.office_extension = request.POST['office_phone_extension']
    contact.email = request.POST.get('email')
    contact.website = request.POST.get('website')
    contact.save(update_fields=['phone', 'phone_extension', 'office_phone', 'office_phone_extension',
                                'cell', 'email', 'website'])
    return contact

def create_employee_contact(request):
    """
    Takes a request and returns a contact
    @param request:
    @return: Contact Object
    """
    phone = request.POST.get('phone')
    cell = request.POST.get('cell')
    email = request.POST.get('email')
    con = Contact(phone=phone, cell=cell, email=email)
    con.save()
    return con


def update_employee_contact(request, contact):
    """
    updates an employee contact object
    @param request: request date
    @param contact: contact object. Validated with get_or_create from view
    @return: updated contact object
    """
    print("CONTACT / TYPE", contact, type(contact))
    contact.phone = request.POST.get('phone')
    contact.cell = request.POST.get('cell')
    contact.email = request.POST.get('email')
    contact.save(update_fields=['phone', 'cell', 'email'])
    return contact


def city_worker(request, city):
    """
    Checks existence of specified City then gets or creates City Object
    @param request:
    @param city:
    @return: City
    """
    c, created = City.objects.get_or_create(city_name=city)
    c.save()
    print "CITY FROM CITY_WORKER", c.city_id
    return c


def boolean_helper(*args):
    """
    Takes boolean from form and handles string passed
    @param args: boolean field from form
    @return: boolean updated to reflect selection
    """
    worker = True
    print('before if boolean', args[0])
    if args[0] is None or args[0] == 'None':
        worker = False
        print('is bus == none', args[0])
    """
    elif args[0] == 'on':
        print('is business == on', args[0])
        worker = True
    """
    return worker


def handle_auto_citys(request):
    """
    Takes city from form and checks if it exists
    @param request:
    @return:
    """
    ac = request.POST.get('city-autocomplete')
    c = request.POST.get('city')
    print("HANDAUTOCITY ac / c", ac, c)

    if ac != '' or ac is not None:
        print "AC IS NOT NONE"
        return ac
    elif c != '' or c is not None:
        print "C IS NONE"
        try:
            c = City.objects.get(pk=c)
        except City.DoesNotExist:
            c = City.objects.get_or_create(city_name=c)
            c.save()
        return c.city_name
    else:
        print "ELSE"
        return "None"


def handle_auto_city(request):
    """
    Takes city from form and checks if it exists
    @param request:
    @return:
    """
    ac = request.POST.get('city-autocomplete')
    c = request.POST.get('city')
    print("HANDAUTOCITY => ac / c", ac, c)

    if ac != '': # or ac is not None:
        print "AC IS NOT NONE: ", ac
        return ac
    elif c != '' or c is not None:
        print "C IS NOT NONE: ", c
        try:
            c = City.objects.get(pk=c)
        except City.DoesNotExist:
            c = City.objects.get_or_create(city_name=c)
            c.save()
        return c.city_name
    else:
        print "ELSE"
        return "None"