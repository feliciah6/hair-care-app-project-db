from models.user import User
from models.saloon import Saloon
from models.services import Service
from models.saloon_services import Saloonservices
from models.register import Register
from models.appointment import Appointment
from peewee import SqliteDatabase, IntegrityError
import datetime
import config

DATABASE = config.DATABASE


def initialize():
    DATABASE.create_tables([User, Saloon, Appointment, Register, Service, Saloonservices], safe=True)
    try:
        User.create(
            user_name="feliciah",
            service="haircare",
            password="qwerty",
            
        )
    except IntegrityError:
        pass

    try:
        Service.create(
            service="manicure",
            price=1000
            
            
        )
    except IntegrityError:
        pass
    try:
        Saloon.create(
              name = "mrembo",
              business_number = "9887",
              opening_time = "10:00am",
              closing_time = "5:00pm",
              description = "urembo services",
              services = "manicure,pedicure,haircare",
              user_id = 1,
              location = 'location'
              
        )
    except IntegrityError:
        pass

    try:
        Register.create(
              user_name = "feliciah",
              email = "lauren@gmail.com",
              phone_number = "0712343647",
              service = "manicure",
              password  = "usgdshssdh",
              confirm_password = "usgdshssdh"
              
              
        )
    except IntegrityError:
        pass
    try:
        Appointment.create(
                  user_id=1,
                  salon_id = 1,
                  services ="haircare,manicure,facial",
                  time_appointment=datetime.datetime.now()
        )
    except IntegrityError:
        pass
    DATABASE.close()