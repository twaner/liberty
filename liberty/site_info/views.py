from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from client.models import Client
from common.models import Address, Contact
from site_info.models import Call_List_Details, Site_Information
from site_info.forms import AddSiteInformationForm, AddCallListDetailsForm
from common.forms import SiteContactForm
from common.helpermethods import create_site_info_contact, update_site_info_contact, validation_helper, form_generator, dict_generator
from site_info.helpermethods import create_call_list_details, create_site_information


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
    Creates a new Site_Information object.
    @param request: request.
    """
    form_list = form_generator(3)
    if request.method == 'POST':
        form_list[0] = AddSiteInformationForm(request.POST)
        form_list[1] = AddCallListDetailsForm(request.POST)
        form_list[2] = SiteContactForm(request.POST)


        # additional site contact info
        show_additional_contact = request.POST.get('showcontact')
        if show_additional_contact != 'None':
            validation = validation_helper(form_list)
            if validation:
                #TODO code to save site
                contact = create_site_info_contact(request)
                call_list_details = create_call_list_details(request, contact)
                site_info = create_site_information(request, call_list_details)

        else:
            # only the first contact
            form_v = form.is_valid()
            form1_v = form1.is_valid()
            form2_v = form2.is_valid()
            if form_v and form1_v and form2_v:
                #TODO code to save site
                contact = create_site_info_contact(request)
                call_list_details = create_call_list_details(request, contact)
                site_info = create_site_information(request, call_list_details)

        return HttpResponseRedirect('/site_infotest/index')

    else:
        form_list[0] = AddSiteInformationForm()
        form_list[1] = AddCallListDetailsForm()
        form_list[2] = SiteContactForm()
        form_dict = dict_generator(form_list)
    return render(request, 'site_info/addsite.html', form_dict)

"""
 if request.method == 'POST':
        form = AddSiteInformationForm(request.POST)
        form1 = AddCallListDetailsForm(request.POST)
        form2 = SiteContactForm(request.POST)
        form3 = AddCallListDetailsForm(request.POST)
        form4 = SiteContactForm(request.POST)
        form_list = [form, form1, form2, form3, form4]

        # additional site contact info
        show_additional_contact = request.POST.get('showcontact')
        if show_additional_contact != 'None':
            validation = validation_helper(form_list)
            if validation:
                #TODO code to save site
                contact = create_site_info_contact(request)
                call_list_details = create_call_list_details(request, contact)
                site_info = create_site_information(request, call_list_details)

        else:
            # only the first contact
            form_v = form.is_valid()
            form1_v = form1.is_valid()
            form2_v = form2.is_valid()
            if form_v and form1_v and form2_v:
                #TODO code to save site
                contact = create_site_info_contact(request)
                call_list_details = create_call_list_details(request, contact)
                site_info = create_site_information(request, call_list_details)

        return HttpResponseRedirect('/site_infotest/index')

    else:
        form = AddSiteInformationForm()
        form1 = AddCallListDetailsForm()
        form2 = SiteContactForm()
        form3 = AddCallListDetailsForm()
        form4 = SiteContactForm()
    return render(request, 'site_info/addsite.html', {'form': form, 'form1': form1, 'form2': form2,
                                                      'form3': form3, 'form4': form4})
                                                      """