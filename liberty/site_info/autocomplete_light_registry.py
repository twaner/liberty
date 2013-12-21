import autocomplete_light
from models import Site_Information


class SiteInformationAutoComplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('site_client',)
    autocomplete_js_attributes = {
        'placeholder': 'Enter a client name',
    }

autocomplete_light.register(Site_Information, SiteInformationAutoComplete)

"""
autocomplete_light.register(Address,
                            #name='AddressAutoCompleteForm',
                            search_fields=['^city.city_name'],
                            #search_fields=['^self.city.city_name'],
                            #choices=Address.objects.all(),
                            autocomplete_js_attributes={'placeholder': 'Enter city name', },
)

autocomplete_light.register(City,
                          #name='CityAutoCompleteForm',
                          search_fields=['^city_name'],
                          autocomplete_js_attributes={'placeholder': 'Enter city name', },)

class AddressAutoComplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('self.city.city_name',)
    autocomplete_js_attributes = {
        'placeholder': 'Enter a city',
    }

class CityAutoComplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ('city.city_name',)
    autocomplete_js_attributes = {
        'placeholder': 'Enter a City'
    }

#autocomplete_light.register(AddressAutoComplete, CityAutoComplete)
                            #AddressAutoCompleteForm, CityAutoCompleteForm)

autocomplete_light.register(City,
                            search_fields=['^city_name'],
                            autocomplete_js_attributes={'placeholder': 'Enter city name', },
)

autocomplete_light.register(City, CityAutoComplete)
autocomplete_light.register(Address, AddressAutoComplete)
"""