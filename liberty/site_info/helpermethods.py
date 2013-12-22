from models import Site_Information, Call_List_Details
from client.models import Client

## CALL LIST HELPERS


def create_call_list_details(request, contact):
    """
    Creates a call list details object
    @param request: request.
    @param args: contact object.
    @return: new call_list_details object.
    """
    call_list_details_type = request.POST.get('call_list_details_type')

    call_order = request.POST.get('call_order')
    enabled = request.POST.get('enabled')
    call_list_contact = contact
    call_list = Call_List_Details(call_list_details_type=call_list_details_type,
                                call_order=call_order, enabled=enabled,
                                call_list_contact=call_list_contact)
    call_list.save()
    return call_list

## SITE INFORMATION HELPERS


def create_site_information(request, details):
    """
    Creates a new site information object.
    @param request: request.
    @param details: Site_Call_List_Details object.
    @return:
    """
    sc = Client.clients.get(pk=request.POST.get('site_client'))
    address_id = Client.clients.get(pk=site_client).address_id

    site_info = Site_Information(site_client=sc, address_id=address_id)
    site_info.save()
    [site_info.site_call_list_details.add(details)]
    site_info.save()
    return site_info
