#Employee models
from django.db import models
from common.models import Person


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
        (INTERN, "INTERN"),
    )
    title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=2, choices=TITLE_CHOICES)

    def __unicode__(self):
        return (self.get_title_display())


class Employee(Person):
    employee_id = models.AutoField(primary_key=True)
    employee_number = models.IntegerField(max_length=10)
    e_title = models.ManyToManyField(Title)
    address = models.ForeignKey('common.Address')
    contact_info = models.ForeignKey('common.Contact')
    hire_date = models.DateField()
    pay_type = models.CharField(max_length=20, blank=True)
    #pay_rate = models.CharField(max_length=20, blank=True)
    pay_rate = models.DecimalField("employee pay rate", max_digits=5, decimal_places=2, blank=True)
    termination_date = models.DateField(null=True, blank=True)
    termination_reason = models.CharField(max_length=300, blank=True)
    #e.e_title.add(t)
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def worker_is(self):
        return (self.e_title)
