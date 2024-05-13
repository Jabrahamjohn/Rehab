#!/usr/bin/python3
import uuid

from sqlalchemy import Column, String, Integer, ForeignKey, Date, Time
from db_storage import db
from sqlalchemy.orm import relationship


class Progress(db.Model):
    __tablename__ = "progress"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'), primary_key=True, nullable=False)
    author = Column(String(36), ForeignKey('therapists.id'), primary_key=True, nullable=False)
    date = Column(Date, nullable=False)
    content = Column(String, nullable=False)

    patients = relationship('Patient', backref='progress')
    therapists = relationship('Therapist', backref='medication')