from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from client.models import Client, Sales_Prospect
from employee.models import Employee
from common.models import Address, Contact, Billing_Information, City
from common.forms import AddressForm, ContactForm, CityForm, CityFormNotAuto, AddressFormNotAuto
from forms import ClientForm, Sales_ProspectForm
from common.helpermethods import create_address, create_contact, city_worker, update_address, update_contact
from client.helpermethods import create_client, create_sales_prospect, update_client, update_sales_prospect

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
    print("CD", client_detail)
    print("BD", business_client)
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


def editclient(request, client_id):
    print("EDITCLIENT CALLED")
    client = Client.clients.get(pk=client_id)
    address = Address.objects.get(pk=client.address_id)
    contact = Contact.objects.get(pk=client.contact_info_id)
    city = City.objects.get(pk=address.city_id)
    #TODO handle billing info
    # Data dictionaries
    client_dict = {'first_name': client.first_name, 'last_name': client.last_name,
                   'business_name': client.business_name, 'is_business': client.is_business,
                   'client_number': client.client_number
    }
    address_dict = {'address': address.address, 'address2': address.address2,
                    'state': address.state, 'zip_code': address.zip_code
    }
    contact_dict = {'phone': contact.phone, 'phone_extension': contact.phone_extension, 'cell': contact.cell,
                    'office_phone': contact.office_phone, 'office_phone_extension': contact.office_phone_extension,
                    'email': contact.email, 'website': contact.website
    }
    city_dict = {'city_name': city.city_name}

    form = ClientForm(request.POST)
    form2 = AddressFormNotAuto(request.POST)
    form3 = ContactForm(request.POST)
    form1 = CityFormNotAuto(request.POST)

    # validation vars
    form_v = form.is_valid()
    form2_v = form2.is_valid()
    form3_v = form3.is_valid()
    form1_v = form1.is_valid()

    # validation
    if form_v and form2_v and form3_v and form1_v:
        # validates =>
        #city_f = request.POST.get('city_name')
        c = city_worker(request, request.POST.get('city_name'))
        a = update_address(request, address, c)
        con = update_contact(request, contact)
        cli = update_client(request, client, a, con)
        return HttpResponseRedirect('/clienttest/index/')
    else:
        # display bound form
        form = ClientForm(client_dict)
        form2 = AddressFormNotAuto(address_dict)
        form3 = ContactForm(contact_dict)
        form1 = CityFormNotAuto(city_dict)
    return render(request, 'client/editclient.html', {'form': form, 'form2': form2, 'form3': form3, 'form1': form1})


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
                return HttpResponseRedirect('/salesprospectindex/index/')
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

    return render(request, 'client/addsalescontact.html',
                  {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})


def editsalesprospect(request, sales_prospect_id):
    sp = Sales_Prospect.objects.get(pk=sales_prospect_id)
    contact = Contact.objects.get(pk=sp.contact_info_id)
    # There does not have to be an address =>
    address = None
    city = None
    try:
        address = Address.objects.get(pk=sp.address_id)
        city = City.objects.get(pk=address.city_id)
    except ObjectDoesNotExist:
        pass
    #data dictionaries
    sp_dict = {'first_name': sp.first_name, 'last_name': sp.last_name, 'liberty_contact': sp.liberty_contact_id,
               'sale_type': sp.sale_type, 'probability': sp.probability, 'initial_contact_date': sp.initial_contact_date,
               'comments': sp.comments
    }
    contact_dict = {'phone': contact.phone, 'phone_extension': contact.phone_extension, 'cell': contact.cell,
                    'office_phone': contact.office_phone, 'office_phone_extension': contact.office_phone_extension,
                    'email': contact.email, 'website': contact.website
    }

    if address is not None:
        address_dict = {'address': address.address, 'address2': address.address2,
                    'state': address.state, 'zip_code': address.zip_code
    }
    else:
        address_dict = {'address': '', 'address2': '',
                    'state': '', 'zip_code': ''}
    if city is not None:
        city_dict = {'city_name': city.city_name}
    else:
        city_dict = {'city_name': ''}
    #submitted form
    if request.method == 'POST':
        form = Sales_ProspectForm(request.POST)
        form1 = CityFormNotAuto(request.POST)
        form2 = AddressFormNotAuto(request.POST)
        form3 = ContactForm(request.POST)
        #check if address is showing
        show_address = request.POST.get('showaddress')
        print("show address value =>", show_address, show_address == None)
        f_valid = form.is_valid()
        f3_valid = form3.is_valid()
        # address is entered
        f1_valid = False
        f2_valid = False
        if show_address is not None:
            # sweet validation
            f1_valid = form1.is_valid()
            f2_valid = form2.is_valid()
        #elif show_address is not None:

        print("Form validation: ", f_valid, "1:", f1_valid, "2:", f2_valid, '3:', f3_valid)

        if f_valid and f1_valid and f2_valid and f3_valid:
            print("WITH ADDRESS")
            c = city_worker(request, request.POST.get('city_name'))
            a = update_address(request, address, c)
            con = update_contact(request, contact)
            update_sales_prospect(request, sp, a, con)
        elif f_valid and (not f1_valid and not f2_valid) and f3_valid:
            print("NO ADDRESS")
            a = None
            con = update_contact(request, contact)
            update_sales_prospect(request, sp, a, con)
        return HttpResponseRedirect('/salesprospectindex/')

    else:
                form = Sales_ProspectForm(sp_dict)
                form1 = CityFormNotAuto(city_dict)
                form2 = AddressFormNotAuto(address_dict)
                form3 = ContactForm(contact_dict)

    return render(request, 'client/editsalesprospect.html',
                  {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})


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