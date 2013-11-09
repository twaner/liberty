from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from client.models import Client, Sales_Prospect
from employee.models import Employee
from common.models import Address, Contact, Billing_Information, City
from common.forms import AddressForm, ContactForm, CityForm, CityFormNotAuto, AddressFormNotAuto
from forms import ClientForm, Sales_ProspectForm
from common.helpermethods import create_address, create_contact, city_worker
from client.helpermethods import create_client, create_sales_prospect

# Basic test
def clienttester(request):
    return HttpResponse("Client Test view working!")

# More advanced test
def detailedClient(request, client_id):
    return HttpResponse("Client id is %s" % client_id)


def index(request):
    client_detail = Client.clients.filter(is_business=False).order_by('last_name')
    business_client = Client.clients.filter(is_business=True).order_by('last_name')
    context = {'client_detail': client_detail, 'business_client': business_client}
    return render(request, 'client/index.html', context)


def detail(request, client_id):
    client_detail = Client.clients.get(pk=client_id)
    address_detail = Address.objects.get(pk=client_detail.address_id)
    contact_detail = Contact.objects.get(pk=client_detail.contact_info_id)
    try:
        billing_detail = Billing_Information.objects.get(pk=client_detail.billing_id)
    except Billing_Information.DoesNotExist:
        billing_detail = None
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

        # debugging
        print("Form validation: ", f_valid, "1:", f1_valid, "2:", f2_valid, '3:', f3_valid)

        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
            #city
            city_f = request.POST.get('city_name')
            c = city_worker(request, city_f)

            # address
            a = create_address(request, c)

            # contact
            con = create_contact(request)

            #client
            create_client(request, a, con)
            return HttpResponseRedirect('/clienttest/index/')
            # good god...just work!
    else:
        form = ClientForm()
        form1 = CityFormNotAuto()
        form2 = AddressFormNotAuto()
        form3 = ContactForm()

    return render(request, 'client/addclient.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})

def add_sales_prospect(request):
    print("Add sales prospect called!")
    if request.method == 'POST':
        form_sp = Sales_ProspectForm(request.POST)
        form_c = CityFormNotAuto(request.POST)
        form_af = AddressFormNotAuto(request.POST)
        form_cf = ContactForm(request.POST)
        # sweet validation
        f_valid = form_sp.is_valid()
        f1_valid = form_c.is_valid()
        f2_valid = form_cf.is_valid()
        f3_valid = form_cf.is_valid()

        print("Form validation: ", f_valid, "1:", f1_valid, "2:", f2_valid, '3:', f3_valid)

        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
            #city
            city_f = request.POST.get('city_name')
            c = city_worker(request, city_f)

            # address
            a = create_address(request, c)

            # contact
            con = create_contact(request)

    else:
        form_sp = Sales_ProspectForm()
        form_c = CityFormNotAuto()
        form_af = AddressFormNotAuto()
        form_cf = ContactForm()

    return render(request, 'client/addclient.html', {'form_sp': form_sp, 'form_c': form_c, 'form_af': form_af, 'form_cf': form_cf})