#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password>@localhost/<databasename>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)