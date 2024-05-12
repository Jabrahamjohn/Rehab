#!/usr/bin/python3
import uuid

from sqlalchemy import Column, String, Integer, ForeignKey
from db_storage import db
from sqlalchemy.orm import relationship


class Patient(db.Model):
    __tablename__ = "patients"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    year = Column(Integer, nullable=False)
    gender = Column(String(6), nullable=False)
    phone_number = Column(String(60), nullable=False)
    email = Column(String(128))
    medical_history = Column(String)
    treatment_plan = Column(String(36), ForeignKey('treatment_plan.id'))
    medication_plan = Column(String(36), ForeignKey('medication.id'))
    progress_notes = Column(String(128))

    treatment_plan = relationship('Treatment_Plan', backref='patients')
    medication = relationship('Medication', backref='patients')