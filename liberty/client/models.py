# Client Model
from django.db import models
from common.models import Person
from employee.models import Employee


class BusinessManager(models.Manager):
    def get_query_set(self):
        return (super(BusinessManager, self).get_query_set().filter(is_business='True'))


class PersonalManager(models.Manager):
    def get_query_set(self):
        return (super(PersonalManager, self).get_query_set().filter(is_business='False'))


class Client(Person):
    client_id = models.AutoField(primary_key=True)
    client_number = models.IntegerField(max_length=10)
    business_name = models.CharField(max_length=50)
    is_business = models.BooleanField(default=False)
    address = models.ForeignKey('common.Address')
    contact_info = models.ForeignKey('common.Contact')
    billing = models.ForeignKey('common.Billing_Information')
    clients = models.Manager()
    personal = PersonalManager()
    businesses = BusinessManager()

    def __unicode__(self):
        if self.is_business == True:
            return (self.business_name)
        else:
            return (u'%s %s' % (self.first_name, self.last_name))


class Sales_Prospect(Person):
    sales_prospect_id = models.AutoField(primary_key=True)
    # TODO - 10/6 - Make this choices
    liberty_contact = models.ForeignKey(Employee)
    sale_type = models.CharField(max_length=40)
    probability = models.CharField(max_length=30)
    initial_contact_date = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=500)

    def __unicode__(self):
        return (u'%s %s' % (self.first_name, self.last_name))


class Billing_Information(models.Model):
    billing_id = models.AutoField(primary_key=True)
    attention_first_name = models.CharField(max_length=30)
    attention_last_name = models.CharField(max_length=30)
    business_name = models.CharField(max_length=30)
    is_business = models.BooleanField(default=False)

    def __unicode__(self):
        if self.is_business == True:
            return (self.business_name)
        else:
            return (u'%s %s' % (self.attention_first_name, self.attention_last_name))



