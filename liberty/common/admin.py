from django.contrib import admin
from common.models import Person, Business, City, State, Address, \
    Contact, Billing_Information, Site, Module_Zone, Equipment

#admin.site.register(Person)
#admin.site.register(Business)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Address)
admin.site.register(Contact)
#admin.site.register(Billing_Informaton)
#admin.site.register(Site)
#admin.site.register(Module_Zone)
admin.site.register(Equipment)