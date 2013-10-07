#Employee models
from django.db import models
from common.models import Person, Address, Contact

class Employee(Person):
	employee_id = models.AutoField(primary_key=True)
	title = models.ManyToManyField(Title)
	address = models.ForeignKey(Address)
	contact_info = models.ForeignKey(Contact)
	hire_date = models.DateField()
	pay_type = models.CharField(max_length=20)
	pay_rate = models.CharField(max_length=20)
	termination_date = models.DateField()
	termination_reason = models.CharField(max_length=300)
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)
	
class Title(models.Model):
	SALES = 'S'
	TECHNICIAN = 'T'
	OFFICE = 'O'
	MARKETING = 'M'
	CONTRACTOR = 'C'
	TITLE_CHOICES = (
		(SALES, "Sales"),
		(TECHNICIAN, "Technician"),
		(OFFICE, "Office"),
		(MARKETING, "Marketing"),
		(CONTRACTOR,"Contractor"),
	)
	title_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=2, choices=TITLE_CHOICES)
	
	def __unicode__(self):
		return self.title
		
	
