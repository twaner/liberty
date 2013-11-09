from django.forms import ModelForm, Textarea
from bootstrap_toolkit.widgets import BootstrapDateInput
from models import Client, Sales_Prospect


class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ('address', 'contact_info', 'billing',)

class Sales_ProspectForm(ModelForm):
    class Meta:
        model = Sales_Prospect
        exclude = ('address', 'contact_info',)