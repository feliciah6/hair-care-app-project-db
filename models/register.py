from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField)

import config
DATABASE= config.DATABASE


class Register(Model):
    user_name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    phone_number = CharField(max_length=100)
    service = TextField()
    password = CharField()
    confirm_password = CharField()

  

    class Meta:
        database = DATABASE