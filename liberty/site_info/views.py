from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from employee.models import Employee, Title
from client.models import Client
from common.models import Address, Contact
from site_info.models import Call_List, Call_List_Details, Site_Information


def testview(self):
    return HttpResponse("Site Info working!")

def testconnection(request, site_id):
    return HttpResponse("Site id is %s" % site_id)

def index(request):
    site_detail = Site_Information.objects.order_by('-site_id')
    context = {'site_detail': site_detail}
    return render(request, 'site_info/indexer.html', context)

def detail(request, site_id):
    site_detail = Site_Information.objects.get(pk=site_id)
    site_worker = Call_List.objects.get(call_list_id == site_detail.site_call_list)
    context = {'site_detail': site_detail, 'site_worker': site_worker}
    return render(request, 'site_info/detail.html', context)


