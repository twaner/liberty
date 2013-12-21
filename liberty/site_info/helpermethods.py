from models import Site_Information, Call_List_Details
from client.models import Client

## CALL LIST HELPERS


def create_call_list_details(request, args):
    """
    Creates a call list details object
    @param request: request.
    @param args: contact object.
    @return: new call_list_details object.
    """
    call_list_details_type = request.POST.get('call_list_details_type')
    call_order = request.POST.get('call_order')
    enabled = request.POST.get('enabled')
    call_list_contact = args[0]

    call_list = Call_List_Details(call_list_details_type=call_list_details_type,
                                call_order=call_order, enabled=enabled,
                                call_list_contact=call_list_contact)
    call_list.save()
    return call_list

    ## SITE INFORMATION HELPERS


def create_site_information(request, args):
    site_client = request.POST.get('site_client')
    site_call_list_details = args[0]
    address_id = Client.clients.get(pk=site_client).address_id

    site_info = (site_client=site_client, address_id=address_id)
    site_info.save()
    return site_info