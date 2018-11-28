from peewee import (Model, CharField,TextField, SqliteDatabase, IntegrityError, IntegerField)

import config
DATABASE= config.DATABASE

class Service(Model):
    services = CharField(max_length=200)
    price = IntegerField()
 
    

    class Meta:
        database = DATABASE


