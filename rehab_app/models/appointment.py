#!/usr/bin/python3
import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Time
from db_storage import db
from sqlalchemy.orm import relationship


class Appointment(db.Model):
    __tablename__ = "appointments"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    duration = Column(Integer, nullable=False)
    patient_id = Column(String(36), ForeignKey('patients.id'),nullable=False)
    therapist_id = Column(String(36), ForeignKey('therapists.id'), nullable=False)