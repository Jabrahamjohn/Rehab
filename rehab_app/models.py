from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Time
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.secret_key = 'AJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@localhost/rehab_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Treatment_Plan(db.Model):
    __tablename__ = "treatment_plans"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    goals = Column(String(255), nullable=False)
    medication_id = Column(String(36), ForeignKey('medication.id'))
    progress_id = Column(String(36), ForeignKey('progress.id'))

    patients = relationship('Patient', backref='treatment_plans')
    medication = relationship('Medication', backref='treatment_plans')
    progress = relationship('Progress', backref='treatment_plans')

class Progress(db.Model):
    __tablename__ = "progress"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    author = Column(String(36), ForeignKey('therapists.reg_no'), nullable=False)
    date = Column(Date, nullable=False)
    content = Column(String(255), nullable=False)

    patients = relationship('Patient', backref='progress')
    therapists = relationship('Therapist', backref='progress')

class Medication(db.Model):
    __tablename__ = "medication"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'))
    name = Column(String(255), nullable=False)
    dosage = Column(String(255), nullable=False)
    frequency = Column(String(60), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    therapist = Column(String(36), ForeignKey('therapists.reg_no'), nullable=False)

    patient = relationship('Patient', back_populates='medications')
    therapists = relationship('Therapist', backref='medications')

class Patient(db.Model):
    __tablename__ = "patients"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    year = Column(Integer, nullable=False)
    gender = Column(String(6), nullable=False)
    phone_number = Column(String(60), nullable=False)
    email = Column(String(128))
    medical_history = Column(String(255))
    treatment_plan_id = Column(String(36), ForeignKey('treatment_plans.id'))
    medication_plan_id = Column(String(36), ForeignKey('medication.id'))
    progress_notes = Column(String(128))

    treatment_plan = relationship('Treatment_Plan', backref='patients')
    medications = relationship('Medication', back_populates='patient')
    progress = relationship('Progress', backref='patient')
    
class User(db.Model):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    phone_number = Column(String(60), nullable=False)
    email = Column(String(128))
    role = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)

    therapist = relationship('Therapist', back_populates='user')


class Therapist(db.Model):
    __tablename__ = "therapists"

    reg_no = Column(String(36), primary_key=True, unique=True, nullable=False)
    availability = Column(String(20), nullable=False)

    user = relationship('User', back_populates='therapist')
    progress = relationship('Progress', backref='therapist')



class Appointment(db.Model):
    __tablename__ = "appointments"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    duration = Column(Integer, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    therapist_id = Column(String(36), ForeignKey('therapists.reg_no'), nullable=False)

    patient = relationship('Patient', backref='appointments')
    therapist = relationship('Therapist', backref='appointments')
