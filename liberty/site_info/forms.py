from django.forms import ModelForm
from django import forms
from models import Call_List_Details, Site_Information
from client.models import Client
from bootstrap_toolkit.widgets import BootstrapDateInput
import autocomplete_light


class AddCallListDetailsForm(ModelForm):
    class Meta:
        model = Call_List_Details
        exclude = ('call_list_contact',)


class AddSiteInformationForm(ModelForm):
    class Meta:
        model = Site_Information
        exclude = ('address', 'contact', 'site_call_list', 'site_call_list_details',)


class AddSiteInformationFormAuto(ModelForm):
    site_client = forms.ModelChoiceField(Client.clients.all(),
    widget=autocomplete_light.TextWidget('Site_InformationSiteInformationAutoComplete'))

    class Meta:
        model = Site_Information
        exclude = ('address', 'contact', 'site_call_list',)



"""
class AddressForm(ModelForm):
    city = forms.ModelChoiceField(City.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('CityAutocomplete'))
"""