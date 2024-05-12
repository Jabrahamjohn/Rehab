#!/usr/bin/python3
import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Time
from db_storage import db
from sqlalchemy.orm import relationship


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