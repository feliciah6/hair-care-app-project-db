from flask import (Flask, render_template, request, jsonify)
from models.saloon import Saloon
from models.register import Register
from models.saloon_services import Saloonservices
from peewee import IntegrityError
from models.services import Service
from models.user import User
from models.appointment import Appointment
# import datetime
from datetime import datetime
app_start_config = {'debug': True, 'port': 8000 , 'host': '0.0.0.0'}
app = Flask(__name__)
import bootstrap
bootstrap.initialize()


@app.route('/')
def index():
    return "List of products"


@app.route('/salon/<services>')
def service(services):
    saloon = Saloon.select().where(Saloon.user_id ** saloon ).get()
    services = Saloonservices.select().where(Saloonservices.user_id==saloon)
    # saloons = Saloon.select().where(Saloon.services.contains(services))
    results = []
    for service in services:
        service = Service.select().where(Service==service).get()
        results.append(
            {
                'services': service.services,
                'price': service.price

            }
            )
    return jsonify(results)
@app.route('/add/services', methods=['POST'])
def add_services():
    data = request.get_json()
    result = {}
    try:
        Service.create(
            services=data.get('services'),
            price=data.get('price')
    
        )
        result = {
        'status': 'success',
        'message': '{} is added'.format(data.get('services'))}
        
        return jsonify(result)
    except IntegrityError:
        result = {
            'status': 'failed',
            'message': '{} is not added'.format(data.get('services'))}
        return jsonify(result)
@app.route('/serviced')
def list_services():
    services = Service.select()
    results = []
    for service in services:   
        results.append(
            {
               'services': service.services,
               'price': service.price
            }
            )
    return jsonify(results)



@app.route('/search/<location>')
def search(location):
    saloons = Saloon.select().where(Saloon.location.contains(location))
    results = []
    for saloon in saloons:
        results.append(
            {
                'name': saloon.name,
                'business_number': saloon.business_number,
                'opening_time': saloon.opening_time,
                'closing_time': saloon.closing_time,
                'description': saloon.description,
                'services': saloon.services,
                'user_id': saloon.user_id,
                'location':saloon.location
             }
            )
    return jsonify(results)
@app.route('/register/user', methods=['POST'])
def register():
    data = request.get_json()
    result = {}
    try:
        Register.create(
            user_name=data.get('user_name'),
            email=data.get('email'),
            phone_number=data.get('phone_number'),
            service=data.get('service'),
            password=data.get('password'),
            confirm_password=data.get('confirm_password'),
        )
        result = {
        'status': 'success',
        'message': '{} registered'.format(data.get('user_name'))}
        
        return jsonify(result)
    except IntegrityError:
        result = {
            'status': 'failed',
            'message': '{} is not unique'.format(data.get('email'))}
        return jsonify(result)

@app.route('/register')
def registered_users():
    registers = Register.select()
    results = []
    for register in registers:
        results.append(
            {
                'user_name': register.user_name,
                'email': register.email,
                'phone_number': register.phone_number,
                'service': register.service,
                'password': register.password,
                'confirm_password': register.confirm_password
            }
        )
    return jsonify(results)
            


@app.route('/user/register', methods=['POST'])
def register_user():
    user_data = request.get_json()
    result = {}
    try:
        User.create(
            user_name=user_data.get('user_name'),
            service=user_data.get('service'),
            password=user_data.get('password')
        )
        result = {
            'status': 'success',
            'message': '{} registered'.format(user_data.get('user_name'))}
        return jsonify(result)
    except IntegrityError:
        result = {
            'status': 'failed',
            'message': '{} is not unique'.format(user_data.get('user_name'))}
        return jsonify(result)


@app.route('/user')
def list_users():
    users = User.select()
    results = []
    for user in users:
        results.append(
            {
                'user_name': user.user_name,
                'service': user.service,
                'password': user.password
            }
        )
    return jsonify(results)



@app.route('/appointment/add', methods=['POST'])
def make_appointment():
    appointment_data = get_json.items()
    time_appointment_raw = appointment_data.get('time_appointment')
    time_appointment_processed = datetime.strptime(time_appointment_raw ,"%m/%d/%Y %H:%M")

    
    Appointment.create(
        user_id=appointment_data.get('user_id'),
        salon_id=appointment_data.get('salon_id'),
        services=appointment_data.get('services'),
        time_appointment=time_appointment_processed
    )
    result = {
        "status": "Success",
        "message": "Appointment set"
        }
    return jsonify(result)


@app.route('/appointment')
def list_appointments():
    appointments = Appointment.select()
    results = []
    for appointment in appointments:
        results.append(
            {
                'user_id': appointment.user_id,
                'time_appointment': appointment.time_appointment,
                'salon_id': appointment.salon_id,
                'services': appointment.services
            }
            )
    return jsonify(results)



@app.route('/saloon/add',  methods=['POST'])
def add_saloon():
    saloon_data = request.get_json()
    Saloon.create(
        name=saloon_data.get('name', 'Anonymous'),
        business_number=saloon_data.get('business_number'),
        opening_time=saloon_data.get('opening_time'),
        closing_time=saloon_data.get('closing_time'),
        description=saloon_data.get('description'),
        services=saloon_data.get('services'),
        user_id=1,
        location=saloon_data.get('location'),

    )
    result = {'status': 'success'}
    return jsonify(result)


@app.route('/saloon',  methods=['GET'])
def list_saloons():
    saloons = Saloon.select()
    results = []
    for saloon in saloons:
        results.append(
            {
                'name': saloon.name,
                'business_number': saloon.business_number,
                'opening_time': saloon.opening_time,
                'closing_time': saloon.closing_time,
                'description': saloon.description,
                'services': saloon.services,
                'user_id': saloon.user_id,
                'location': saloon.location,
             }
            )
    return jsonify(results)

if __name__ == '__main__':
    app.run(**app_start_config)