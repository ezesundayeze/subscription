import unittest
from app import CustomerEntity, WebsiteEntity, PlanEntity
from peewee import DoesNotExist, IntegrityError


class CreateCustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer = CustomerEntity("Eze Sunday", "naira123?", "r@gmail.com", 5, "2020-02-21 06:35:45.658505")

    def test_create_customer(self):
        self.assertEqual("Account created successfully", self.customer.create()["message"])

    def tearDown(self):
        self.customer.delete()
        
class UpgradeCustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = CustomerEntity("Eze Sunday", "naira123?", "hello@gmail.com", 5, "2020-02-21 06:35:45.658505")

    def test_upgrade_customer(self):
        self.assertEqual("Your plan has been upgraded Successfully", self.customer.upgrade()["message"] )

class DeleteCustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = CustomerEntity("Eze Sunday", "naira123?", "mailsforeze@gmail.com", 5, "2020-02-21 06:35:45.658505")
        self.customer.create()

    def test_delete_customer(self):
        self.assertEqual("Customer deleted successfully", self.customer.delete()["message"])

class CreateWebsiteTest(unittest.TestCase):
    def setUp(self):
        self.website = WebsiteEntity("google.com", 1)

    def test_create_customer(self):
        self.assertEqual("Website created successfully", self.website.create()["message"])

    def tearDown(self):
        self.website.delete()

    





        


            


        

    # def test_upgrade_customer(self):
    #     customer = CustomerEntity("Eze Sunday", "naira123?", "mailstoeze@gmail.com", 5, "2020-02-21 06:35:45.658505")
    #     customer.upgrade()

    # def test_delete_customer(self):
    #     customer = CustomerEntity("Eze Sunday", "naira123?", "mailstoeze@gmail.co9  m", 5, "2020-02-21 06:35:45.658505")
    #     customer.delete()

class PlanTest(unittest.TestCase):
    pass



