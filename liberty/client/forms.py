from django.forms import ModelForm, Textarea
from bootstrap_toolkit.widgets import BootstrapDateInput
from models import Client, Sales_Prospect

"""
Form for adding a client.
"""
class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ('address', 'contact_info', 'billing',)

"""
Form for adding a sales prospect.
"""
class Sales_ProspectForm(ModelForm):
    class Meta:
        model = Sales_Prospect
        exclude = ('address', 'contact_info', 'is_client',)
        widgets = {
            'initial_contact_date': BootstrapDateInput, 'termination_date': BootstrapDateInput,
            'comments': Textarea(attrs={'cols': 160, 'rows': 10})
        }