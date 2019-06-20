from peewee import *


database = MySQLDatabase('imagify1', **{'charset': 'utf8', 'use_unicode': True, 'host': 'localhost', 'user': 'eze', 'passwd': '.Naira123?'})


class BaseModel(Model):
    class Meta:
        database = database


class Plan(BaseModel):
    name = CharField(max_length=300, unique=True)
    price = DecimalField(max_digits=10, decimal_places=5)
    quantity = IntegerField()

    class Meta:
        table_name = 'plan'

class Customer(BaseModel):
    name = CharField(max_length=300)
    password = CharField(max_length=300)
    email_address = CharField(max_length=300, unique=True)
    plan = ForeignKeyField(Plan, backref='plan',
                                    column_name='plan', null=True)
    renewal_date = DateTimeField(null=True)

    class Meta:
        table_name = 'customer'


class Website(BaseModel):
    url = CharField(default="example.com", max_length=300)
    customer = ForeignKeyField(Customer, backref="customer", column_name="customer", default=1, on_delete="CASCADE")

    class Meta:
        table_name = 'website'