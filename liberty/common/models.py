# Common models
from django.db import models

# Choices
STATE_CHOICES = (
    ('Alabama', 'AL'),
    ('Alaska', 'AK'),
    ('Arizona', 'AZ'),
    ('Arkansas', 'AR'),
    ('California', 'CA'),
    ('Colorado', 'CO'),
    ('Connecticut', 'CT'),
    ('Delaware', 'DE'),
    ('District of Columbia', 'DC'),
    ('Florida', 'FL'),
    ('Georgia', 'GA'),
    ('Hawaii', 'HI'),
    ('Idaho', 'ID'),
    ('Illinois', 'IL'),
    ('Indiana', 'IN'),
    ('Iowa', 'IA'),
    ('Kansas', 'KS'),
    ('Kentucky', 'KY'),
    ('Louisiana', 'LA'),
    ('Maine', 'ME'),
    ('Maryland', 'MD'),
    ('Massachusetts', 'MA'),
    ('Michigan', 'MI'),
    ('Minnesota', 'MN'),
    ('Mississippi', 'MS'),
    ('Missouri', 'MO'),
    ('Montana', 'MT'),
    ('Nebraska', 'NE'),
    ('Nevada', 'NV'),
    ('New Hampshire', 'NH'),
    ('New Jersey', 'NJ'),
    ('New Mexico', 'NM'),
    ('New York', 'NY'),
    ('North Carolina', 'NC'),
    ('North Dakota', 'ND'),
    ('Ohio', 'OH'),
    ('Oklahoma', 'OK'),
    ('Oregon', 'OR'),
    ('Pennsylvania', 'PA'),
    ('Rhode Island', 'RI'),
    ('South Carolina', 'SC'),
    ('South Dakota', 'SD'),
    ('Tennessee', 'TN'),
    ('Texas', 'TX'),
    ('Utah', 'UT' ),
    ('Vermont', 'VT'),
    ('Virginia', 'VA'),
    ('Washington', 'WA'),
    ('West Virginia', 'WV'),
    ('Wisconsin', 'WI'),
    ('Wyoming', 'WY'),
)

# Entity Models
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class Business(models.Model):
    name = models.CharField("business name", max_length=30)

    class Meta:
        abstract = True

# Location Information
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30)

    def __unicode__(self):
        return (self.city_name)


class State(models.Model):
    STATES = (
        ('Alabama', 'AL'),
        ('Alaska', 'AK'),
        ('Arizona', 'AZ'),
        ('Arkansas', 'AR'),
        ('California', 'CA'),
        ('Colorado', 'CO'),
        ('Connecticut', 'CT'),
        ('Delaware', 'DE'),
        ('District of Columbia', 'DC'),
        ('Florida', 'FL'),
        ('Georgia', 'GA'),
        ('Hawaii', 'HI'),
        ('Idaho', 'ID'),
        ('Illinois', 'IL'),
        ('Indiana', 'IN'),
        ('Iowa', 'IA'),
        ('Kansas', 'KS'),
        ('Kentucky', 'KY'),
        ('Louisiana', 'LA'),
        ('Maine', 'ME'),
        ('Maryland', 'MD'),
        ('Massachusetts', 'MA'),
        ('Michigan', 'MI'),
        ('Minnesota', 'MN'),
        ('Mississippi', 'MS'),
        ('Missouri', 'MO'),
        ('Montana', 'MT'),
        ('Nebraska', 'NE'),
        ('Nevada', 'NV'),
        ('New Hampshire', 'NH'),
        ('New Jersey', 'NJ'),
        ('New Mexico', 'NM'),
        ('New York', 'NY'),
        ('North Carolina', 'NC'),
        ('North Dakota', 'ND'),
        ('Ohio', 'OH'),
        ('Oklahoma', 'OK'),
        ('Oregon', 'OR'),
        ('Pennsylvania', 'PA'),
        ('Rhode Island', 'RI'),
        ('South Carolina', 'SC'),
        ('South Dakota', 'SD'),
        ('Tennessee', 'TN'),
        ('Texas', 'TX'),
        ('Utah', 'UT'),
        ('Vermont', 'VT'),
        ('Virginia', 'VA'),
        ('Washington', 'WA'),
        ('West Virginia', 'WV'),
        ('Wisconsin', 'WI'),
        ('Wyoming', 'WY'),
    )
    #state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=2, choices=STATES)

    def __unicode__(self):
        return (self.state)


class Address(models.Model):
    address = models.CharField("address", max_length=30)
    address2 = models.CharField("address 2", max_length=30, blank=True)
    city = models.ForeignKey(City)
    state = models.CharField(max_length=30, choices=STATE_CHOICES, default='NY')
    #state = models.ForeignKey(State)
    zip_code = models.CharField("zip code", max_length=10)
    #zip_code = models.IntegerField("zip code", max_length=10)

    def __unicode__(self):
        return (u'%s %s %s %s %s' % (self.address, self.address2,
                                     self.city.city_name, self.state, self.zip_code))

# Info Models
class Contact(models.Model):
    phone = models.CharField("primary phone", max_length=13, blank=True)
    phone_extension = models.CharField("primary phone extension", max_length=10, blank=True)
    cell = models.CharField("cell phone", max_length=12, blank=True)
    office_phone = models.CharField("office phone", max_length=13, blank=True)
    office_phone_extension = models.CharField("office phone extension", max_length=10, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return "%s%s%s-%s%s%s-%s%s%s%s" % tuple(self.phone)


class Billing_Information(models.Model):
    billing_id = models.AutoField(primary_key=True)
    #client = models.ForeignKey('client.client', related_name="")
    attention_first_name = models.CharField(max_length=30, blank=True)
    attention_last_name = models.CharField(max_length=30, blank=True)
    business_name = models.CharField(max_length=35, blank=True)
    is_business = models.BooleanField(default=False)

    def __unicode__(self):
        if self.is_business == True:
            return (self.business_name)
        else:
            return (u'%s %s' % (self.attention_first_name, self.attention_last_name))


# LibertyModels
class Site(models.Model):
    address = models.ForeignKey(Address)
    contact = models.ForeignKey(Contact)

    class Meta:
        abstract = True


class Module_Zone(models.Model):
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    number = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=50, blank=True)
    part_number = models.CharField(max_length=50, blank=True)
    serial_number = models.CharField(max_length=30, blank=True)
    install_date = models.DateField(null=True, blank=True)
    install_tech = models.ForeignKey('employee.Employee')
    service = models.ForeignKey('site_info.Service_Information', verbose_name="service instance")

    class Meta:
        abstract = True


class Equipment(models.Model):
    equipment_name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    equipment_notes = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return (self.equipment_name)

