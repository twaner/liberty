from django.test import TestCase
import datetime as dt
from common.models import Address, City, State, Contact, Billing_Information
from client.models import Client, Sales_Prospect

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

        # contact info
        con = Contact.objects.create(phone="876123409876",
                                     phone_extension="4444",
                                     cell="09812345678", email="test@test.com",
                                     website="www.test.com")
        con.save()

        # Client
        cl = Client(first_name="Steve", last_name="Jones", client_number=4545)
        cl.save()

        testa = Address(address="54 Tester St",address2="Apt 2b", city=c,
                        state=s, zip_code=12409)

        testa.save()

        # Client Address and Contact Info
        aa = Address(address="44 Test Ave", address2="Unit 2", city=c,
                    state=s, zip_code=12408)
        aa.save()

        cl.address = aa

        cl.billing = Billing_Information(attention_first_name=cl.first_name,
                                         attention_last_name=cl.last_name)
        cl.save()

    def test_client_exist(self):
        client = Client.clients.get(client_number=4545)
        self.assertTrue(client.first_name== "Steve")


