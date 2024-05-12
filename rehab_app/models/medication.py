#!/usr/bin/python3
import uuid

from sqlalchemy import Column, String, Integer, ForeignKey, Date, Time
from db_storage import db
from sqlalchemy.orm import relationship


class Medication(db.Model):
    __tablename__ = "medication"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'), primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    dosage = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    therapist = Column(String(36), ForeignKey('therapists.id'), primary_key=True, nullable=False)

    patients = relationship('Patient', backref='medication')
    therapists = relationship('Therapist', backref='medication')