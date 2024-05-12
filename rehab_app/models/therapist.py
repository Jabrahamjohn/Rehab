#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, ForeignKey
from db_storage import db
from sqlalchemy.orm import relationship


class Therapist(db.Model):
    __tablename__ = "therapists"

    id = Column(String(36), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    phone_number = Column(String(60), nullable=False)
    email = Column(String(128))
    availability = Column(String(20), nullable=False)
