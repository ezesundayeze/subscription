# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Plan(peewee.Model):
    name = CharField(max_length=300)
    price = DecimalField(auto_round=False, decimal_places=5, max_digits=10, rounding='ROUND_HALF_EVEN')
    quantity = IntegerField()
    class Meta:
        table_name = "plan"


@snapshot.append
class Customer(peewee.Model):
    name = CharField(max_length=300)
    password = CharField(max_length=300)
    email_address = CharField(default='hello@gmail.com', max_length=300)
    plan = snapshot.ForeignKeyField(backref='plan', column_name='plan', index=True, model='plan', null=True)
    renewal_date = DateTimeField()
    class Meta:
        table_name = "customer"


@snapshot.append
class Website(peewee.Model):
    url = CharField(default='example.com', max_length=300)
    customer = snapshot.ForeignKeyField(backref='customer', column_name='customer', index=True, model='customer')
    class Meta:
        table_name = "website"


