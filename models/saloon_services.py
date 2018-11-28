from peewee import (Model, CharField,TextField, SqliteDatabase, IntegrityError, IntegerField)

import config
DATABASE= config.DATABASE

class Saloonservices(Model):
    user_id = IntegerField()
    services= CharField()

    class Meta:
        database = DATABASE