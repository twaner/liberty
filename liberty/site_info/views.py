from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from employee.models import Employee, Title
from client.models import Client
from common.models import Address, Contact
from site_info.models import Site_Contact, Site_Information


def testview(self):
    return HttpResponse("Site Info working!")

def testconnection(request, site_id):
    return HttpResponse("Site id is %s" % site_id)

def index(request):
    site_detail = Site_Information.objects.order_by('-site_id')
    context = {'site_detail': site_detail}
    return render(request, 'site_info/index.html', context)