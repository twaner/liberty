# Common models
from django.db import models

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
        ('Utah', 'UT' ),
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
    address2 = models.CharField("address 2", max_length=30)
    city = models.CharField("city", max_length=30)
    state = models.ForeignKey(State, )
    zip_code = models.IntegerField("zip code", max_length=10)

    def __unicode__(self):
        return (u'%s %s %s %s s%' % (self.address, self.address2, self.city, self.state.state, self.zip_code))

# Info Models
class Contact(models.Model):
    phone = models.CharField("primary phone", max_length=13)
    phone_extension = models.CharField("primary phone extension", max_length=10)
    cell = models.CharField("cell phone", max_length=12)
    phone = models.CharField("office phone", max_length=13)
    phone_extension = models.CharField("office phone extension", max_length=10)
    email = models.EmailField()
    website = models.URLField()


class Billing_Information(models.Model):
    billing_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return (self.billing_id)

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
    manufacturer = models.CharField(max_length=50)
    part_number = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=30)
    install_date = models.DateField()
    install_tech = models.ForeignKey('employee.Employee')
    service = models.ForeignKey('site_info.Service_Information', verbose_name="service instance")

    class Meta:
        abstract = True


class Equipment(models.Model):
    equipment_name = models.CharField(max_length=100)
    equipment_type = models.CharField(max_length=100)
    equipment_notes = models.CharField(max_length=1000)

    def __unicode__(self):
        return (self.equipment_name)
