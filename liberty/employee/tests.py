"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from common.models import Address, City, State, Contact
from employee.models import Employee

# TESTING VARIABLES
first_name = "Tom"
last_name = "Jane"
employee_number = 1234
hire_date = 2013 - 9 - 10
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
                                   city="Kingston", state=s, zip_code=12401)
        a.save()

        # contact info
        con = Contact.objects.create(phone="876123409876",
                                     phone_extension="4444",
                                     cell="09812345678", email="test@test.com",
                                     website="www.test.com")
        con.save()

        #
        # employee
        Employee.objects.create(first_name="Tom", last_name="Jane",
                                employee_number=1234, address_id=a.id,
                                contact_info_id=con,
                                hire_date=2013 - 9 - 10, pay_type="hourly",
                                pay_rate="20.00")
        e.save()

    def test_employee_exist(self):
        employee = Employee.objects.get(employee_number=1234)
        self.assertEqual(employee.pay_type(),pay_type,
                         "Pay type doesnt match")

