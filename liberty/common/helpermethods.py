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
    zip_code = request.POST.get('zip_code')
    a = Address(address=address, address2=address2, city=city, state=state,
                zip_code=zip_code)
    a.save()
    return a


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

def city_worker(request, city):
    """
    Checks existence of specified City then gets or creates City Object
    @param request:
    @param city:
    @return: City
    """
    c, created = City.objects.get_or_create(city_name=city)
    c.save()
    return c


def boolean_helper(*args):
    """
    Takes boolean from form and handles string passed
    @param args: boolean field from form
    @return: boolean
    """
    worker = True
    print('before if boolean', args[0])
    if args[0] == 'None':
        worker = False
        print('is bus == none', args[0])
    """
    elif args[0] == 'on':
        print('is business == on', args[0])
        worker = True
    """
    return worker

def handle_auto_city(request):
    """
    Takes city from form and checks if it exists
    @param request:
    @return:
    """
    ac = request.POST.get('city-autocomplete')
    c = request.POST.get('city')
    if ac != '':
        print "AC IS NOT NONE"
        return ac
    elif c != '':
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
    if ac != '':
        print "AC IS NOT NONE"
        return ac
    elif c != '':
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