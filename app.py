from models import Customer, Plan, Website
import datetime
from peewee import DoesNotExist, IntegrityError

class CustomerEntity:
    """ 
    This class allows the customer to manage their account, create their account, delete their account, and upgrade or downgrade their account and plan
    """

    def __init__(self, _name, _password, _email,  _plan, _renewal_date):
        self.name = _name
        self.password = _password
        self.email = _email
        self.plan = _plan
        self.renewal_date = _renewal_date

    def create(self):
        try:
            customer = Customer.create(name=self.name, password=self.password, email=self.email, plan=self.plan, renewal_date=self.renewal_date)
            customer.save()
        except IntegrityError:
            return {"message":"Customer already exist"}        

    def delete(self):
        try:
            Customer.get(email_address=self.email)
            customer =  Customer.delete().where(Customer.email_address==self.email)
            customer.execute()
            return {"message":"Customer deleted successfully"}
        except DoesNotExist:
            return {"message":"Customer does not exist"}

    def upgrade(self):
        try:
            customer = Customer.get(email_address=self.email)
        except DoesNotExist:
            return {"message":"Customer does not exist"}

        else:
            customer = Customer.update(plan=self.plan, renewal_date=self.renewal_date).where(Customer.email_address==self.email)
            customer.execute()
            return  {"message":"Create Customer Created Successfully"}


class WebsiteEntity:

    def __init__(self, _url, _customer):
        self.url =_url
        self.customer = _customer

    def create(self):
        """ check customers plan and limit them to the number of website that's accordigng to their plan"""
        "check customers plan, check customers website count"
        try:
            customer = Customer.get(id=self.customer)
        except DoesNotExist:
            return {"message":"Customer does not exist"}
        
        website_count = Website.select().where(Website.url==self.url).count()
        print(website_count, customer.plan.quantity)
        if customer.plan.quantity != 0 and customer.plan.quantity > website_count and customer.renewal_date!=None:
            website =  Website(url=self.url, customer=self.customer)
            website.save()
            message = "Website created successfully"
            return {"message":message}

        if customer.plan.quantity==0 and customer.renewal_date!=None:
            website =  Website(url=self.url, customer=self.customer)
            website.save()
            message = "Website created successfully"
            print("hi")
            return {"message":message}

        if customer.renewal_date==None:
            return {"message":"Sorry, your plan has expired" }

        else:
            return {"message":"Sorry, you can't add more websites, your have exceeded your subscription limit"}

 


    def delete(self):
        try:
            Website.get(url=self.url)
            Website.delete().where(Website.customer==self.customer).execute()
        except DoesNotExist:
            if DoesNotExist:
                return {"message":"Website does not exist"}
        

    def update(self):
        try:
            Website.get(url=self.url)
        except DoesNotExist:
            if DoesNotExist:
                return {"message":"Website does not exist"}
        else:
            Website.update(url=self.url).where(Website.customer==self.customer).returning(Website)
            return {"message":"Wesite updated successfully"}

class PlanEntity:
    """ 
    This class allows the Admin to manage subscription plans
    """
    def __init__(self, _name, _price, _quantity):
        self.price = _price
        self.quantity = _quantity
        self.name = _name
    

    def create(self):
        try:
            plan = Plan.create(name=self.name, price=self.price, quantity=self.quantity)
            plan.save()
        except IntegrityError:
            return {"message":"Plan already exist"}

    def delete(self):
        pass

    def update(self):
        plan = Plan.update(name=self.name, price=self.price, quantity=self.quantity).where(Plan.name==self.name)
        plan.execute()

def expire_plan():
    """
    This function periodically check customers plan and expire them if their renewal date is less than todays date.his process can be run periodically with celery, celerybeat and RabbitMQ
    """
    customers = Customer.select()
    for customer in customers:
        if customer.renewal_date >= datetime.datetime.now():
            Customer.update(renewal_date=None).where(Customer.renewal_date==customer.renewal_date).execute()
            print("expired")
            return {"message":"Expired on"}




""" 
A user selects a plan and then will be asked to provide further information to create his account and to complete his susbcription
"""

"""
The input here will generally be either from a select input tag or any other ui element that willl be populated from the database
However, for this test, I am allowing the user to type the name of the plan by hand.
"""

def create_customer():
    package = input("Choose a Package: single, plus or infinite:")
    try:
        plan =  Plan.get(name=package)
    except DoesNotExist:
        return {"message":"The package you selected does not exist"}
    else:
        customer =  CustomerEntity("Eze Sunday", "naira123?", "mailstoeze@gmail.com", plan.id, "2020-02-21 06:35:45.658505" )
        create = customer.create()
        print(create["message"])

def delete_customer():
    customer =  CustomerEntity("Eze Sunday", "naira123?", "mailstoeze@gmail.com", 5, "2020-02-21 06:35:45.658505" )
    delete = customer.delete()
    print(delete["message"])


def upgrade_plan():
    package = input("Choose a Package: single, plus or infinite:")
    try:
        plan =  Plan.get(name=package)
    except DoesNotExist:
        print("The package you selected does not exist")
    else:
        customer =  CustomerEntity("Eze Sunday", "naira123?", "mailstoeze@gmail.com", plan.id, "2030-02-21 06:35:45.658505" )
        upgrade = customer.upgrade()
        print(upgrade["message"])


def delete_website():
    website = WebsiteEntity("eze.com", 1)
    delete = website.delete()
    print(delete["message"])

website = WebsiteEntity("eze.com", 2)
update = website.create()
print(update["message"])


plan = PlanEntity("booster", 89, 5)
create = plan.create()
print(create["message"])














