from django import forms
from django.forms import ModelForm, Textarea
from models import Address, City, Contact
import autocomplete_light
import autocomplete_light_registry

# ModelForms
class AddressForm(ModelForm):
    city = forms.ModelChoiceField(City.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('CityAutocomplete'))

    class Meta:
        model = Address
        #widgets = {'city': autocomplete_light.get_widgets_dict(City)}

    """
    def __init__(self, *args, **kwargs):
        try:
            print("ARGS[CITY]", args[0]['city'])
            print("ARGS[CITYAUTO]", args[0]['city-autocomplete'])
            pass
        except ValueError:
            pass

        c1 = args[0]['city']
        c2 = args[0]['city-autocomplete']
        try:
            # convert
            valid_city = self.city
        except ValueError:
            # new city
            valid_city = self.city
        for k, v in kwargs.iteritems():
            print("KWARGS:", k, v)
        city = kwargs.pop('c')

        print("CITY FROM kwargs.pop:", city)

        super(AddressForm, self).__init__(*args, **kwargs)
        # determine what city is pk or name

        self.fields['city'] = city
        print("SELF.FIELDS[CITY]", self.fields["city"])
        for i in self.fields:
            print i
        """


class AddressForm1(ModelForm):
    city = forms.ModelChoiceField(City.objects.all(),
                                  widget=autocomplete_light.ChoiceWidget('CityAutocomplete')
    )

    class Meta:
        model = Address


class AddressFormNotAuto(ModelForm):
    class Meta:
        model = Address
        exclude = ('city',)


class AddressFormPlaces(ModelForm):
    class Meta:
        model = Address
        exclude = ('city',)
        widgets = {
            'state': Textarea(attrs={'cols': 40, 'rows': 1})}


class CityFormNotAuto(ModelForm):
    class Meta:
        model = City


class ContactForm(ModelForm):
    class Meta:
        model = Contact


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


class EmployeeContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('phone_extension', 'office_phone', 'office_phone_extension', 'website',)

