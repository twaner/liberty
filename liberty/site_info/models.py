# Site_Info models
from django.db import models
from datetime import datetime, timedelta
from common.models import Site, Module_Zone, Equipment, Person

# CALL LIST
class Call_List_Details(models.Model):
    GENERAL = 'G'
    BURG = 'B'
    FIRE = 'F'
    MEDICAL = 'M'
    ENVIRONMENTAL = 'E'
    ALTERNATE = 'A'
    ALTERNATE2 = 'A2'
    CALL_LIST_TYPE = (
        (GENERAL, 'General Call List'),
        (BURG, "Burg Call List"),
        (FIRE, 'Fire Call List'),
        (MEDICAL, 'Medical Call List'),
        (ENVIRONMENTAL, 'Environmental Call List'),
        (ALTERNATE, 'Alternate Call List'),
        (ALTERNATE2, 'Alternate Call List 2'),
    )

    call_list_details_id = models.AutoField(primary_key=True)
    call_list_details_type = models.CharField(max_length=2, choices=CALL_LIST_TYPE)
    order = models.CharField(max_length=30)
    enabled = models.BooleanField(default=False)
    call_list_contact = models.ForeignKey('common.Contact', null=True, blank=True)

def __unicode__(self):
    return self.get_call_list_details_type_display()
#return(u'%s %s' % (self.first_name, self.last_name))


class Call_List(Person):
    call_list_id = models.AutoField(primary_key=True)
    # call_list_detail = models.ForeignKey('Call_List_Details', verbose_name="call list list details",
    #                                      null=True, blank=True)
    # NEW
    #call_list_contact = models.ForeignKey('common.Contact', null=True, blank=True)
    call_list_details = models.ManyToManyField(Call_List_Details,
                                               verbose_name="Call list(s)")

    def __unicode__(self):
        return u'%s' % (self.call_list_detail.get_call_list_details_type_display())

# REGION	 SITE INFORMATION
class Site_Information(Site):
    site_id = models.AutoField(primary_key=True)
    # specific info for the client - not related to call list
    site_client = models.ForeignKey('client.client', verbose_name="Client Site")
    #q = si.site_call_list.all()
    #si.site_call_list.add(cl)
    site_call_list = models.ManyToManyField('Call_List')

    def __unicode__(self):
        return u'%s %s' % (self.site_client.first_name, self.site_client.last_name)

# PANEL OBJECT
class Panel(Equipment):
    panel_id = models.AutoField(primary_key=True)
    #equipment_type = models.CharField(default='panel')
    panel_name = models.CharField(max_length=100, blank=True)

#TODO - 10/6 - Get additional panel fields

# REGION LOCATIONAL INFORMATION
class Module(Module_Zone):
    module_id = models.AutoField(primary_key=True)
    module_panel_alarm = models.ForeignKey('Panel')
    module_site = models.ForeignKey('Site_Information')

    #TODO - 10/6 - Better return info?
    def __unicode__(self):
        return (self.name)


class Zone(Module_Zone):
    zone_id = models.AutoField(primary_key=True)
    zones_panel_alarm = models.ForeignKey('Panel')
    zone_site = models.ForeignKey('Site_Information')

    #TODO - 10/6 - Better return info?
    def __unicode__(self):
        return (self.name)

# REGION EQUIPMENT
#BASE OBJECT
class Site_Equipment(Equipment):
    equipment_id = models.AutoField(primary_key=True)
    equipment_site = models.ForeignKey('Site_Information')

# CAMERA OBJECT
class Camera(Equipment):
    camera_id = models.AutoField(primary_key=True)
    #self.equipment_type = models.CharField(default='camera')
    camera_name = models.CharField(max_length=100)
    DVR_type = models.CharField(max_length=100, blank=True)
    communication_type = models.CharField(max_length=300, blank=True)


# Panel gets its location from zone or module table
class Site_Panel(models.Model):
    site_panel_id = models.AutoField(primary_key=True)
    panel_site = models.ForeignKey('Site_Information')
    # TODO - 10/6 choices or own table
    site_panel_panel = models.ForeignKey('Panel')
    communication_id = models.CharField(max_length=20)


class Site_Camera(models.Model):
    site_camera_id = models.AutoField(primary_key=True)
    camera_site = models.ForeignKey('Site_Information')
    camera = models.ForeignKey(Camera)
    location = models.CharField(max_length=100, blank=True)


# REGION SERVICE
# Instance of service on equipment
class Service_Information(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_panel = models.ForeignKey('Panel')
    technician = models.ForeignKey('employee.Employee')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    notes = models.CharField(max_length=1000)

# TODO - Table for installation information
class Installation_Information(models.Model):
    installation_id = models.AutoField(primary_key=True)
    installation_site = models.ForeignKey('Site_Information')
    installation_tech = models.ManyToManyField('employee.Employee')
    panels_installed = models.ManyToManyField(Panel, related_name="panels")
    cameras_installed = models.ManyToManyField(Camera, related_name="cameras")
    additional_equipment = models.ManyToManyField('common.Equipment')
    #installation_date = models.DateField()
    installation_start_time = models.DateTimeField(null=True, blank=True)
    installation_end_time = models.DateTimeField(null=True, blank=True)


def _get_install_time(self):
    dt = self.installation_start_time - self.installation_end_time
    days, seconds = dt.days, dt.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    #seconds = seconds % 60
    return ('{hours}:{minutes}'.format(hours, minutes))


installation_duration = property(_get_install_time)

