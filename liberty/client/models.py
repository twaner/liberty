# Client Model
from django.db import models
from common.models import Person
from employee.models import Employee

# USE 0 == False // 1 == True!
class BusinessManager(models.Manager):
    def get_query_set(self):
        """
        Model manager for commercial accounts.
        Filters clients on is_business boolean.
        @return: query set of commercial accounts.
        """
        return super(BusinessManager, self).get_query_set().filter(is_business='1')


class PersonalManager(models.Manager):
    def get_query_set(self):
        """
        Model manager for residential accounts.
        Filters clients on is_business boolean.
        @return: query set of residential accounts.
        """
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
        """
        Sets display for Client object to first and last name.
        @return: first and last name of Client.
        """
        if self.is_business:
            return self.business_name
        else:
            return u'%s %s' % (self.first_name, self.last_name)

    def is_a_business(self):
        """
        Checks if a client is a commercial account.
        @return: Business name or first name of the client.
        """
        if self.is_business:
            return self.business_name
        else:
            return self.first_name


class Sales_Prospect(Person):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    UNKNOWN = 'U'
    PROBABILITY = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
        (UNKNOWN, 'Unknown'),
    )
    sales_prospect_id = models.AutoField(primary_key=True)
    liberty_contact = models.ForeignKey('employee.Employee', null=True, blank=True)
    sale_type = models.CharField(max_length=40, blank=True)
    probability = models.CharField(max_length=20, choices=PROBABILITY, blank=True)
    initial_contact_date = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=500, blank=True)
    address = models.ForeignKey('common.Address', verbose_name="prospect address", null=True, blank=True)
    contact_info = models.ForeignKey('common.Contact', verbose_name="prospect contact", null=True, blank=True)
    # 11-9 changed to is_client from if_client
    # business logic should transfer information to client if true!
    is_client = models.BooleanField(default=False)

    def __unicode__(self):
        """
        Sets display for Sales_Prospect object to first and last name.
        @return: first and last name of Sales_Prospect.
        """
        return u'%s %s' % (self.first_name, self.last_name)






