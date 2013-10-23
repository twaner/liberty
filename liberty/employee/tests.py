"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import datetime as dt
from common.models import Address, City, State, Contact
from employee.models import Employee, Title

# TESTING VARIABLES
first_name = "Tom"
last_name = "Jane"
employee_number = 1234
#hire_date = (2010, 1, 1)
pay_type = "hourly"
pay_rate = "20.00"


class SimpleTest(TestCase):
    def setUp(self):
        #Create data for other tables
        s = State.objects.create(state="NY")
        s.save()
        c = City.objects.create(city_name="Kington")
        c.save()
        a = Address.objects.create(address="23 Test Lane", address2="Apt 8",
                                   city=c, state=s, zip_code=12401)
        a.save()

        d = str(dt.datetime.now())[:10]

        # contact info
        con = Contact.objects.create(phone="876123409876",
                                     phone_extension="4444",
                                     cell="09812345678", email="test@test.com",
                                     website="www.test.com")
        con.save()

        #
        # employee
        t = Title.objects.create(title="T")
        t.save()

        Employee.objects.create(first_name="Tom", last_name="Jane",
                                employee_number=1234, address=a,
                                contact_info=con, termination_date='2013-10-09',
                                hire_date='2013-08-09', pay_type="hourly",
                                pay_rate=20.00)
        e = Employee.objects.get(employee_number=1234)
        e.save()
        e.employee_title_name.add(t)
        e.save()
        #e.save()

    def test_employee_exist(self):
        employee = Employee.objects.get(employee_number=1234)
        self.assertEqual(employee.pay_type, pay_type,
                         "Pay type doesnt match")


    def test_worker_is(self):
        e = Employee.objects.get(employee_number=1234)
        e.save()
        f = e.worker_is()
        self.assertEqual(f, "T", "Employee title doesn't match")

