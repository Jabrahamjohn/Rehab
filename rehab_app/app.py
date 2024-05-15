#!/usr/bin/env python3

from flask import render_template, request, redirect, url_for, flash, session, jsonify
from models import app, Treatment_Plan, Progress, Medication, Patient, Therapist, Appointment
from models import db

with app.app_context():
    #Create all the db models into the database
    db.create_all()


@app.route('/')
def index():
    """Renders the index.html template with a title."""
    title = 'Rehab Center Management System'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    """Renders the about.html template."""
    return render_template('about.html')

@app.route('/services')
def services():
    """Renders the services.html template."""
    return render_template('services.html')

@app.route('/contact')
def contact():
    """Renders the contact.html template."""
    return render_template('contact.html')

@app.route('/resources')
def resources():
    """Renders the resources.html template."""
    return render_template('resources.html')

@app.route('/privacystatement')
def privacystatement():
    """Renders the privacystatement.html template."""
    return render_template('privacystatement.html')

@app.route('/virtualtour')
def virtualtour():
    """Renders the virtualtour.html template"""
    return render_template('virtualtour.html')

@app.route('/admissions')
def admissions():
    """Renders the admissions.html template"""
    return render_template('admissions.html')

@app.route('/login')

@app.route('/dashboard')
def dashboard():
    #if not session.get("logged_in"):
     #   return redirect(url_for("login"))
    """Renders the dashboard.html template"""
    return render_template('./dashboard/dashboard.html')

@app.route('/patients')
def patients():
    """Renders the patients.html template"""
    patients = Patient.query.all()
    return render_template('./dashboard/patients.html', patients=patients)

@app.route('/appointments')
def appointments():
    """Renders the appointments.html template"""
    return render_template('./dashboard/appointments.html')

@app.route('/document')
def document():
    """Renders the document.html template"""
    return render_template('./dashboard/document.html')

@app.route('/messaging')
def messaging():
    """Renders the messaging.html template"""
    return render_template('./dashboard/messaging.html')

@app.route('/notification')
def notifications():
    """Renders the notifications.html template"""
    return render_template('./dashboard/notification.html')

@app.route('/reports')
def reports():
    """Renders the reports.html template"""
    return render_template('./dashboard/medication.html')

@app.route('/tasks')
def tasks():
    """Renders the tasks.html template"""
    return render_template('./dashboard/tasks.html')

@app.route('/logout')
def logout():
    #session.pop("logged_in", None)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.secret_key = 'AJ'
    app.run(debug=True)
