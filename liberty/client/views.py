from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from client.models import Client, Sales_Prospect
from employee.models import Employee
from common.models import Address, Contact, Billing_Information, City
from common.forms import AddressForm, ContactForm, CityForm, CityFormNotAuto, AddressFormNotAuto
from forms import ClientForm

# Basic test
def clienttester(request):
    return HttpResponse("Client Test view working!")

# More advanced test
def detailedClient(request, client_id):
    return HttpResponse("Client id is %s" % client_id)


def index(request):
    client_detail = Client.clients.order_by('-client_id')
    context = {'client_detail': client_detail}
    return render(request, 'client/indexer.html', context)


def detail(request, client_id):
    client_detail = Client.clients.get(pk=client_id)
    address_detail = Address.objects.get(pk=client_detail.address_id)
    contact_detail = Contact.objects.get(pk=client_detail.contact_info_id)
    billing_detail = Billing_Information.objects.get(pk=client_detail.billing_id)

    context = {'client_detail': client_detail, 'address_detail': address_detail,
               'contact_detail': contact_detail, 'billing_detail': billing_detail}
    return render(request, 'client/detail.html', context)


def addclient(request):
    print("Add client view called")
    #forms
    if request.method == 'POST':
        form = ClientForm(request.POST)
        form1 = CityFormNotAuto(request.POST)
        form2 = AddressFormNotAuto(request.POST)
        form3 = ContactForm(request.POST)
        # sweet validation
        f_valid = form.is_valid()
        f1_valid = form1.is_valid()
        f2_valid = form2.is_valid()
        f3_valid = form3.is_valid()
        c = City
        print("Form validation: ", f_valid, "1:", f1_valid, "2:", f2_valid, '3:', f3_valid)
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
            # get address, city, contact to create employee
            city_f = request.POST.get('city_name')
            # does city already exist?
            if City.objects.filter(city_name__icontains=city_f).count() > 1:
                # city name is in db -> get pk to add to address model
                global c
                print("In if")
                c = City.objects.get(city_name__icontains=city_f)
            else:
                # create a new city object
                global c
                print("In else")
                c = City(city_name=city_f)
                c.save()

            # address
            address = request.POST.get('address')
            address2 = request.POST.get('address2')
            state = request.POST.get('state')
            zip_code = request.POST.get('zip_code')
            a = Address(address=address, address2=address2, city=c.city_id, state=state,
                        zip_code=zip_code)
            a.save()

            # contact
            phone = request.POST.get('phone')
            phone_extension = request.POST.get('phone_extension')
            cell = request.POST.get('cell')
            office = request.POST['office_phone']
            office_extension = request.POST('office_phone_extension')
            email = request.POST.get('email')
            website = request.POST.get('')
            con = Contact(phone=phone, phone_extension=phone_extension, cell=cell, email=email,
                          office_phone=office, office_extension=office_extension, website=website)
            con.save()

            #client
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            client_number = request.POST('client_number')
            business_name = request.POST('business_name')
            is_business = request.POST('is_business')

            client = Client(first_name=first_name, last_name=last_name, client_number=client_number,
                            business_name=business_name, is_business=is_business, address=a, contact_info=con)
            client.save()
            # good god...just work!
    else:
        form = ClientForm()
        form1 = CityFormNotAuto()
        form2 = AddressFormNotAuto()
        form3 = ContactForm()

    return render(request, 'addclient.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})
