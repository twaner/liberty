from django import forms
from django.forms import ModelForm, Textarea
from models import Address, City, Contact
import autocomplete_light
import autocomplete_light_registry

# Address Forms ##
class AddressForm(ModelForm):
    city = forms.ModelChoiceField(City.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('CityAutocomplete'))

    class Meta:
        model = Address
        #widgets = {'city': autocomplete_light.get_widgets_dict(City)}


class AddressFormNotAuto(ModelForm):
    class Meta:
        model = Address
        exclude = ('city',)


class AddressFormPlaces(ModelForm):
    class Meta:
        model = Address
        exclude = ('city',)


## City Forms ##

class CityFormNotAuto(ModelForm):
    class Meta:
        model = City




class CityForm(ModelForm):
    city = forms.ModelChoiceField(City.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget("CityAutocomplete"))

    class Meta:
        model = City

    def is_valid(self):
        # parent validation
        valid = super(CityForm, self).is_valid()

        # check if valid
        if valid:
            #TODO add handling
            pass
            #if self.city_name != '':

## Contact Forms ##
class ContactForm(ModelForm):
    class Meta:
        model = Contact


class EmployeeContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('phone_extension', 'office_phone', 'office_phone_extension', 'website',)


class SiteContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('cell', 'email', 'office_phone', 'office_phone_extension', 'website',)