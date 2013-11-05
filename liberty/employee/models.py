#Employee models
from django.db import models
#from django import forms
from django.forms import ModelForm, Textarea
from common.models import Person
from bootstrap_toolkit.widgets import BootstrapDateInput


class Title(models.Model):
    SALES = 'S'
    TECHNICIAN = 'T'
    OFFICE = 'O'
    MARKETING = 'M'
    CONTRACTOR = 'C'
    INTERN = 'I'
    TITLE_CHOICES = (
        (SALES, "Sales"),
        (TECHNICIAN, "Technician"),
        (OFFICE, "Office"),
        (MARKETING, "Marketing"),
        (CONTRACTOR, "Contractor"),
        (INTERN, "Intern"),
    )
    title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=2, choices=TITLE_CHOICES)

    def __unicode__(self):
        return self.get_title_display()


class Employee(Person):
    """COM = 'COM',
    HR = 'HR',
    SAL = 'SAL',
    OT = 'OT', """
    PAY_TYPE_CHOICES = (
        ('COM', 'Commission'),
        ('HR', 'Hourly'),
        ('SAL', 'Salary'),
        ('OT', 'Other'),
    )
    employee_id = models.AutoField(primary_key=True)
    employee_number = models.IntegerField(max_length=10)
    e_title = models.ManyToManyField(Title, verbose_name="Employee Title(s)")
    address = models.ForeignKey('common.Address')
    contact_info = models.ForeignKey('common.Contact')
    hire_date = models.DateField()
    pay_type = models.CharField(max_length=3, choices=PAY_TYPE_CHOICES, default='HR')
    pay_rate = models.DecimalField("employee pay rate", max_digits=10, decimal_places=2, blank=True)
    termination_date = models.DateField(null=True, blank=True)
    termination_reason = models.CharField(max_length=300, blank=True)
    #e.e_title.add(t)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def worker_is(self):
        return (self.e_title)

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