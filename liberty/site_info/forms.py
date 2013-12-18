from models import Call_List, Call_List_Details, Site_Information
from django.forms import ModelForm, Textarea
from bootstrap_toolkit.widgets import BootstrapDateInput


class AddCallListDetailsForm(ModelForm):
    class Meta:
        model = Call_List_Details
        exclude = ('call_list_contact',)

class AddCallListForm(ModelForm):
    class Meta:
        model = Call_List
        exclude = ('call_list_details', )

class AddSiteInformationForm(ModelForm):
    class Meta:
        model = Site_Information
        exclude = ('address', 'contact', 'site_call_list',)