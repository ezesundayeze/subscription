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
        self.website = WebsiteEntity("eze.com", 1)

    def test_create_website(self):
        self.assertEqual("Website created successfully", self.website.create()["message"])

    def tearDown(self):
        self.website.delete()

class UpdateWebsiteTest(unittest.TestCase):
    def setUp(self):
        self.website = WebsiteEntity("google.com", 1)

    def test_update_website(self):
        self.assertEqual("Wesite updated successfully", self.website.update()["message"] )


class DeleteWebsiteTest(unittest.TestCase):
    def setUp(self):
        self.website = WebsiteEntity("yahoo.com", 1)
        self.website.create()

    def test_delete_website(self):
        self.assertEqual("Website deleted successfully", self.website.delete()["message"])


class CreatePlanTest(unittest.TestCase):
    def setUp(self):
        self.plan = PlanEntity("Silver", 57, 7)

    def test_create_plan(self):
        self.assertEqual("Plan created successfully", self.plan.create()["message"])

    def tearDown(self):
        self.plan.delete()


class UpdatePlanTest(unittest.TestCase):
    def setUp(self):
        self.plan = PlanEntity("gold", 57, 7)

    def test_update_plan(self):
        self.assertEqual("Plan updated successfully", self.plan.update()["message"] )

class DeletePlanTest(unittest.TestCase):
    def setUp(self):
        self.plan = PlanEntity("silver", 57, 7)
        self.plan.create()
    
    def test_deletePlan(self):
        self.assertEqual("Plan deleted successfully", self.plan.delete()["message"])

    
class ExpirePlanTest(unittest.TestCase):
    




        


            


        

    # def test_upgrade_customer(self):
    #     customer = CustomerEntity("Eze Sunday", "naira123?", "mailstoeze@gmail.com", 5, "2020-02-21 06:35:45.658505")
    #     customer.upgrade()

    # def test_delete_customer(self):
    #     customer = CustomerEntity("Eze Sunday", "naira123?", "mailstoeze@gmail.co9  m", 5, "2020-02-21 06:35:45.658505")
    #     customer.delete()

class PlanTest(unittest.TestCase):
    pass



