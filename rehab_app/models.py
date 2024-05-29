from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from flask_login import UserMixin

app = Flask(__name__)

app.secret_key = 'super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/rehab_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#mysql = MySQL(app)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(300), nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    therapist_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=True)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(50), nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    current_occupancy = db.Column(db.Integer, nullable=False, default=0)

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    maintenance_schedule = db.Column(db.DateTime, nullable=False)
    last_maintenance = db.Column(db.DateTime, nullable=True)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    position = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    last_updated = db.Column(db.DateTime, nullable=False)

class MaintenanceSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=False)
    schedule_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)