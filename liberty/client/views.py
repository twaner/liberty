from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from client.models import Client, Sales_Prospect
from employee.models import Employee
from common.models import Address, Contact, Billing_Information

# Basic test
def clienttester(request):
    return HttpResponse("Client Test view working!")

# More advanced test
def detailedClient(request, client_id):
    return HttpResponse("Client id is %s" % client_id)

def index(request):
    client_detail = Client.clients.order_by('-client_id')
    context = {'client_detail': client_detail}
    return render(request, 'client/index.html', context)

def detail(request, client_id):
    client_detail = Client.clients.get(pk=client_id)
    address_detail = Address.objects.get(pk=client_detail.address_id)
    contact_detail = Contact.objects.get(pk=client_detail.contact_info_id)
    billing_detail = Billing_Information.objects.get(pk=client_detail.billing_id)

    context = {'client_detail': client_detail, 'address_detail': address_detail,
               'contact_detail': contact_detail, 'billing_detail': billing_detail}
    return render(request, 'client/detail.html', context)