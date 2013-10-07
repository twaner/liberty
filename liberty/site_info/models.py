# Site_Info models
from django.db import models
from datetime import datetime, timedelta
from common.models import Person, Business, Contact, Site, Module_Zone, Equipment
from employee.models import Employee

# REGION	 SITE INFORMATION
class Site(Site):
	site_id = models.AutoField(primary_key=True)
	call_list = models.ManyToManyField(Call_List)
	contact = models.ForeignKey(Contact)
	
	def __unicode__(self):
		return(self.name)
	
class Call_List(models.Model)
	GENERAL = 'G'
	BURG = 'B'
	FIRE = 'F'
	MEDICAL = 'M'
	ENVIRONMENTAL = 'E'
	ALTERNATE = 'A'
	ALTERNATE2 = 'A2'
	CALL_LIST_TYPE(
		(GENERAL, 'General Call List'),
		(BURG, 'Burg Call_List List'),
		(FIRE, 'Fire Call List'),
		(MEDICAL, 'Medical Call List'),
		(ENVIRONMENTAL, 'Environmental Call List'),
		(ALTERNATE, 'Alternate Call List'),
		(ALTERNATE2, 'Alternate Call List 2'),
	)

	call_list_id = models.AutoField(primary_key=True)
	call_list_type = models.CharField(max_length=2,choices=CALL_LIST_TYPE)
	site = models.ForeignKey(Site)
	call_order = models.CharField(max_length=30)
	enabled = models.BooleanField(default=False)
	
	def __unicode__(self):
		return(self.call_list_type)
		#return(u'%s %s' % (self.first_name, self.last_name))

# REGION LOCATIONAL INFORMATION
class Module(Module_Zone):
	module_id = models.AutoField(primary_key)
	module_panel_alarm = models.ForeignKey(Panel_Information)

	#TODO - 10/6 - Better return info?
	def __unicode__(self):
		return(self.name)
	
class Zone(Module_Zone):
	zone_id = models.AutoField(primary_key=True)
	zones_panel_alarm = models.ForeignKey(Panel_Information)

	#TODO - 10/6 - Better return info?
	def __unicode__(self):
		return(self.name)

# REGION EQUIPMENT
#BASE OBJECT
class Site_Equipment(Equipment):
	equipment_id = models.AutoField(primary_key=True)
	equipment_site = models.ForeignKey(Site)
	
# CAMERA OBJECT
class Camera(Equipment):
	camera_id = models.AutoField(primary_key=True)
	self.equipment_type = models.CharField(default='camera')
	camera_name = models.CharField(max_length=100)
	DVR_type = models.CharField(max_length=100)
	communication_type = models.CharField(max_length=300)
	
# PANEL OBJECT
class Panel(Equipment):
	panel_id = models.AutoField(primary_key=True)
	self.equipment_type = models.CharField(default='camera')
	panel_name = models.CharField(max_length=100)
	#TODO - 10/6 - Get additional panel fields

# Panel gets its location from zone or module table
class Site_Panel(models.Model):
	site_panel_id = models.AutoField(primary_key=True)
	panel_site = models.ForeignKey(Site)
	# TODO - 10/6 choices or own table
	panel_type = models.ForeignKey(Panel)
	communication_id = models.CharField(max_length=20)
	
class Site_Camera(models.Model):
	site_camera_id = models.AutoField(primary_key=True)
	camera_site = models.ForeignKey(Site)
	location = models.CharField(max_length=100)
	
		
# REGION SERVICE
# Instance of service on equipment
class Service_Information(models.Model):
	service_id = models.AutoField(primary_key=True)
	service_panel_alarm = models.ForeignKey(Panel_Information)
	techician = models.ForeignKey(Employee)
	start_time = models.DateTime()
	end_time = models.DateField()
	note	s = models.CharField(max_length=1000)
	
# TODO - Table for installation information
class Installation_Information(models.Model)
	installation_id = models.AutoField(primary_key=True)
	installation_site = models.ForeignKey(Site)
	installation_tech = models.ManyToManyField(Employee)
	panels_installed = models.ManyToManyField(Panel)
	cameras_installed = models.ManyToManyField(Camera)
	additional_equipment = models.ManyToManyField(Equipment)
	installation_date = models.DateField()
	installation_start_time = models.DateTime()
	installation_end_time = models.DateTime()
	
	def get_install_time(self):
		dt =self.installation_start_time - self.installation_end_time
		days, seconds = dt.days, dt.seconds
		hours = days * 24 + seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60
		return('{hours}:{minutes}'.format(hours,minutes))
		
	instalation_duration = property(_get_install_time)
		
