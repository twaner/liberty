# Client Model
from django.db import models
from common.models import Person
from employee.models import Employee

# USE 0 == False // 1 == True!
class BusinessManager(models.Manager):
    def get_query_set(self):
        return super(BusinessManager, self).get_query_set().filter(is_business='1')


class PersonalManager(models.Manager):
    def get_query_set(self):
        return super(PersonalManager, self).get_query_set().filter(is_business='0')


class Client(Person):
    client_id = models.AutoField(primary_key=True)
    client_number = models.IntegerField(max_length=10)
    business_name = models.CharField(max_length=50, blank=True)
    is_business = models.BooleanField(default=False)
    address = models.ForeignKey('common.Address', null=True, blank=True)
    contact_info = models.ForeignKey('common.Contact', null=True, blank=True)
    billing = models.ForeignKey('common.Billing_Information', null=True, blank=True)
    # managers Client.'manager'.get()
    clients = models.Manager()
    personal = PersonalManager()
    businesses = BusinessManager()

    def __unicode__(self):
        if self.is_business:
            return self.business_name
        else:
            return u'%s %s' % (self.first_name, self.last_name)

    def is_a_business(self):
        if self.is_business:
            return self.business_name
        else:
            return self.first_name


class Sales_Prospect(Person):
    sales_prospect_id = models.AutoField(primary_key=True)
    # TODO - 10/6 - Make this choices and Optional
    liberty_contact = models.ForeignKey('employee.Employee', null=True, blank=True)
    sale_type = models.CharField(max_length=40, blank=True)
    probability = models.CharField(max_length=30, blank=True)
    initial_contact_date = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=500, blank=True)
    address = models.ForeignKey('common.Address', verbose_name="prospect address", null=True, blank=True)
    contact_info = models.ForeignKey('common.Contact', verbose_name="prospect contact", null=True, blank=True)
    if_client = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)






