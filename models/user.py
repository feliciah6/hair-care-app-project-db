from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField)

import config
DATABASE= config.DATABASE


class User(Model):
    user_name = CharField(max_length=100)
    service = CharField(max_length=100)
    password = CharField(max_length=100, unique=True)
  

    class Meta:
        database = DATABASE
