from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from client.models import Client
from common.models import Address, Contact
from site_info.models import Call_List, Call_List_Details, Site_Information
from site_info.forms import AddSiteInformationForm, AddCallListForm, AddCallListDetailsForm
from common.forms import AddressForm, SiteContactForm, AddressFormPlaces, CityFormNotAuto
from common.helpermethods import city_worker, create_address, create_employee_contact, handle_auto_city, update_address,update_employee_contact

def testview(self):
    return HttpResponse("Site Info working!")


def testconnection(request, site_id):
    return HttpResponse("Site id is %s" % site_id)


def index(request):
    """
    Index view of site information.
    @param request: request.
    @return: rendered index view of site info.
    """
    site_detail = Site_Information.objects.order_by('-site_id')
    context = {'site_detail': site_detail}
    return render(request, 'site_info/index.html', context)


def detail(request, site_id):
    """
    Returns detailed view of a site.
    @param request: request.
    @param site_id: site pk.
    @return: rendered site detail view.
    """
    site_detail = Site_Information.objects.get(pk=site_id)
    site_worker = Call_List.objects.get(call_list_id == site_detail.site_call_list)
    context = {'site_detail': site_detail, 'site_worker': site_worker}
    return render(request, 'site_info/detail.html', context)


def addsiteinfo(request):
    """
    Creates new site.
    @param request: request.
    """
    if request.method == 'POST':
        form = AddSiteInformationForm(request.POST)
        form1 = AddCallListForm(request.POST)
        form2 = AddCallListDetailsForm(request.POST)
        form3 = SiteContactForm(request.POST)

        return HttpResponseRedirect('/site_infotest/index')
    else:
        form = AddSiteInformationForm()
        form1 = AddCallListForm()
        form2 = AddCallListDetailsForm()
        form3 = SiteContactForm()
    return render(request, 'site_info/addsite.html', { 'form': form, 'form1': form1, 'form2': form2,
                                         'form3': form3, })