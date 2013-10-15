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