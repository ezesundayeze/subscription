from models import Customer, Plan, Website
import datetime
from peewee import DoesNotExist, IntegrityError
import re
class CustomerEntity:
    """ 
    This class allows the customer to manage their account, create their account, delete their account, and upgrade or downgrade their account and plan
    """

    def __init__(self, _name, _password, _email,  _plan, _renewal_date):
        self.name = _name.lower()
        self.password = _password
        self.email = _email.lower()
        self.plan = _plan
        self.renewal_date = _renewal_date

    def create(self):
        try:
            plan = Plan.get(id=self.plan)
            customer = Customer.create(name=self.name, password=self.password, email_address=self.email, plan=plan.id, renewal_date=self.renewal_date)
            customer.save()
        except IntegrityError:
            
            return {"message":"Customer already exist"}
        else:
            return {"message":"Account created successfully"}       

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
            plan = Plan.get(id=self.plan)
        except (Customer.DoesNotExist, Plan.DoesNotExist,):
            if Customer.DoesNotExist:
                return {"message":"Customer does not exist"}
            if Plan.DoesNotExist:
                return {"message":"Plan does not exist"}
        else:
            customer = Customer.update(plan=plan.id, renewal_date=self.renewal_date).where(Customer.email_address==self.email)
            customer.execute()
            return  {"message":"Your plan has been upgraded Successfully"}


class WebsiteEntity:
    """ 
    This allows the user to create websites according to their plan
    """


    def __init__(self, _url, _customer):
        self.url =_url.lower()
        self.customer = _customer
        self.pattern = "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"


    def create(self):
        """ check customers plan and limit them to the number of website that's accordigng to their plan"""
        "check customers plan, check customers website count"

        
        if re.match(self.pattern, self.url, flags=0):
            try:
                customer = Customer.get(id=self.customer)
            except DoesNotExist:
                return {"message":"Customer does not exist"}
            
            website_count = Website.select().where(Website.customer==customer.id).count()
            if customer.plan.quantity != 0 and customer.plan.quantity > website_count and customer.renewal_date!=None:
                website =  Website(url=self.url, customer=self.customer)
                website.save()
                message = "Website created successfully"
                return {"message":message}

            if customer.plan.quantity==0 and customer.renewal_date!=None:
                website =  Website(url=self.url, customer=self.customer)
                website.save()
                message = "Website created successfully"
                return {"message":message}

            if customer.renewal_date==None:
                return {"message":"Sorry, your plan has expired" }

            else:
                return {"message":"Sorry, you can't add more websites, your have exceeded your subscription limit"}
        else:
            return {"message":"Invalid website"}

    def delete(self):
        try:
            Website.get(url=self.url)
            if Website.delete().where((Website.customer==self.customer) and (Website.url==self.url)).execute():
                return {"message":"Website deleted successfully"}
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
        self.name = _name.lower()
    

    def create(self):
        try:
            plan = Plan.create(name=self.name, price=self.price, quantity=self.quantity)
            plan.save()
            return {"message":"Plan created successfully"}
        except IntegrityError:
            return {"message":"Plan already exist"}

    def delete(self):
        try:
            plan = Plan.delete().where(Plan.name==self.name)
            plan.execute()
            return {"message":"Plan deleted successfully"}
        except DoesNotExist:
            return {"message":"Plan does not exist"}

    def update(self):
        try:
            get_plan = Plan.get(name=self.name)
            plan = Plan.update(name=self.name, price=self.price, quantity=self.quantity).where(Plan.name==get_plan.name)
            plan.execute()
            return {"message":"Plan updated successfully"}
        except Plan.DoesNotExist:
            if Plan.DoesNotExist:
                return {"message":"Plan does not exist"}


def expire_plan():
    """
    This function periodically check customers plan and expire them if their renewal date is less than todays date.his process can be run periodically with celery, celerybeat and RabbitMQ
    """
    customers = Customer.select()
    for customer in customers:
        if customer.renewal_date >= datetime.datetime.now():
            Customer.update(renewal_date=None).where(Customer.renewal_date==customer.renewal_date).execute()
            return {"message":"Plan expired"}
        else:
            return {"message":"All plans are active"}












