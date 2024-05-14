#!/usr/bin/python3

#models.py
import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Time
from extensions import db
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


class Appointment(db.Model):
    __tablename__ = "appointments"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    duration = Column(Integer, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'),nullable=False)
    therapist_id = Column(String(36), ForeignKey('therapists.id'), nullable=False)

class Medication(db.Model):
    __tablename__ = "medication"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    therapist_id = Column(String(36), ForeignKey('therapists.id'), nullable=False)  # Specify therapist_id as foreign key

    patients = relationship('Patient', backref='patient_medications', foreign_keys=[patient_id])  # Change backref to 'patient_medications'
    therapists = relationship('Therapist', backref='medication')

class Patient(db.Model):
    __tablename__ = "patients"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    year = Column(Integer, nullable=False)
    gender = Column(String(6), nullable=False)
    phone_number = Column(String(60), nullable=False)
    email = Column(String(128))
    medical_history = Column(String)
    #treatment_plan = Column(String(36), ForeignKey('treatment_plan.id'))
    #medication_plan = Column(String(36), ForeignKey('medication.id'))
    progress_notes = Column(String(128))

    #treatment_plan = relationship('Treatment_Plan', backref='treatment_plan_patients')
    medication = relationship('Medication', backref='patient', foreign_keys='Medictaion.patient_id')

class Therapist(db.Model):
    __tablename__ = "therapists"

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    phone_number = Column(String(60), nullable=False)
    email = Column(String(128))
    availability = Column(String(20), nullable=False)

class Treatment_Plan(db.Model):
    __tablename__ = "treatment_plans"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    goals = Column(String,nullable=False)
    medication = Column(String(128), ForeignKey('medication.id'))
    progress = Column(String(128), ForeignKey('progress.id'))

    patients = relationship('Patient', backref='treatment_plans')
    medication = relationship('Medication', backref='treatment_plans')
    progress = relationship('Progress', backref='treatment_plans')

class Progress(db.Model):
    __tablename__ = "progress"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'), primary_key=True, nullable=False)
    author = Column(String(36), ForeignKey('therapists.id'), primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    content = Column(String, nullable=False)

    patients = relationship('Patient', backref='progress')
    therapists = relationship('Therapist', backref='medication')