import unittest
from django.test import TestCase
from employee.models import Employee, Title
from common.models import Address, City, Contact

class EmployeeTest(TestCase):
    # This is the fixture:
    #- fields:
    # model: employee
    fixtures = ['employee.json']

    def testEmployee(self):
        e = Employee.objects.get(pk=1)
        self.assertEquals(s.first_name, 'Johnny')


# Samples tests
class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1


class TestBasic2(unittest.TestCase):
    "Show setup and teardown"

    def setUp(self):
        self.a = 1

    def tearDown(self):
        del self.a

    def test_basic1(self):
        "Basic with setup"

        self.assertNotEqual(self.a, 2)

    def test_basic2(self):
        "Basic2 with setup"
        assert self.a != 2

    def test_fail(self):
        "This test should fail"
        assert self.a == 1