from models import Employee, Title
from django.forms import ModelForm, Textarea
from bootstrap_toolkit.widgets import BootstrapDateInput


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # exclude foreign keys
        exclude = ('address', 'contact_info',)
        """
        hire_date = forms.DateField(
            widget=BootstrapDateInput(),
        )"""
        widgets = {
            'hire_date': BootstrapDateInput, 'termination_date': BootstrapDateInput,
            'termination_reason': Textarea(attrs={'cols': 160, 'rows': 10})
        }


class AddEmployeeForm(EmployeeForm):
    class Meta(EmployeeForm.Meta):
        exclude = ('address', 'contact_info', 'termination_date', 'termination_reason',)


class TitleForm(ModelForm):
    class Meta:
        model = Title


