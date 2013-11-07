from django import forms
from django.forms import ModelForm
from models import Address, City, Contact
import autocomplete_light

# ModelForms
class AddressForm(ModelForm):
    city = forms.ModelChoiceField(City.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('CityAutocomplete')
    )

    class Meta:
        model = Address


class AddressFormNotAuto(ModelForm):
    class Meta:
        model = Address
        exclude = ('city',)

class CityFormNotAuto(ModelForm):
    class Meta:
        model = City


class ContactForm(ModelForm):
    class Meta:
        model = Contact


class CityForm(ModelForm):
    city = forms.ModelChoiceField(City.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget("CityAutoComplete"))

    class Meta:
        model = City


class EmployeeContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('phone_extension', 'office_phone', 'office_phone_extension', 'website',)

