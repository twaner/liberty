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
        #print("Form validation: ", f_valid, "1:", f1_valid, "2:", f2_valid, '3:', f3_valid)

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

def addsalesprospect(request):
    print("Add sales prospect called!")
    if request.method == 'POST':
        form = Sales_ProspectForm(request.POST)
        form1 = CityFormNotAuto(request.POST)
        form2 = AddressFormNotAuto(request.POST)
        form3 = ContactForm(request.POST)
        #check if address is showing
        show_address = request.POST.get('showaddress')
        print("show address value", show_address)
        f_valid = form.is_valid()
        f3_valid = form3.is_valid()
        # address is entered
        if show_address != 'None':
            # sweet validation
            f1_valid = form1.is_valid()
            f2_valid = form2.is_valid()

            print("Form validation: ", f_valid, "1:", f1_valid, "2:", f2_valid, '3:', f3_valid)

            if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
                #city
                city_f = request.POST.get('city_name')
                c = city_worker(request, city_f)
                # address
                a = create_address(request, c)
                # contact
                con = create_contact(request)
                #sales prospect
                create_sales_prospect(address=a, contact_info=con)

                #handle success!
                return HttpResponseRedirect('/clienttest/index/')
        # no address entered
        print("Form validation: ", f_valid, "3: ", f3_valid)
        if f_valid and f3_valid:
            con = create_contact(request)
            create_sales_prospect(request, con)

    else:
        form = Sales_ProspectForm()
        form1 = CityFormNotAuto()
        form2 = AddressFormNotAuto()
        form3 = ContactForm()

    return render(request, 'client/addsalescontact.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})


def salesprospectindex(request):
    sales_prospect_detail = Sales_Prospect.objects.all().order_by('last_name')
    context = {'sales_prospect_detail': sales_prospect_detail}
    return render(request, 'client/salesprospectindex.html', context)


def salesprospectdetails(request, sales_prospect_id):
    sales_prospect_detail = Sales_Prospect.objects.get(pk=sales_prospect_id)
    try:
        address_detail = Address.objects.get(pk=sales_prospect_detail.address_id)
    except Address.DoesNotExist:
        address_detail = None
    contact_detail = Contact.objects.get(pk=sales_prospect_detail.contact_info_id)
    context = {'sales_prospect_detail': sales_prospect_detail, 'address_detail': address_detail,
               'contact_detail': contact_detail}
    print(sales_prospect_detail)
    return render(request, 'client/salesprospectdetail.html', context)


"""
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
"""