#!/usr/bin/env python3

#app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from flask_migrate import Migrate


app = Flask(__name__)
app.secret_key = 'AJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@localhost/rehab'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

from models import Appointment, Medication, Patient, Therapist, Treatment_Plan, Progress

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

@app.route('/login' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == STAFFPASSWORD:
            #session["logged_in"] = True
            return redirect(url_for('change_password'))
        else:
            error_message="Invalid password or user name. Please try again!"
            return render_template("login.html", error_message=error_message)
    """Renders the login.html template"""
    return render_template('login.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
   # if not session.get("logged_in"):
    #    return redirect(url_for("login"))
    if request.method == "POST":
        # Logic to change password
        initial_password = request.form.get("initial_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")
        if initial_password == STAFFPASSWORD:
            if new_password == confirm_password:
                STAFFPASSWORD = new_password
                return redirect(url_for("/dashboard"))
            else:
                error_message = "New password and confirm password do not match. Please try again!"
                return render_template("change_password.html", error_message=error_message)
        else:
            error_message = "Invalid initial password. Please try again!"
            return render_template("change_password.html", error_message=error_message)
    """Renders the change_password.html template"""
    return render_template('change_password.html')



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

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    new_patient = patients(name=name, year=age)
    db.session.add(new_patient)
    db.session.commit()
    flash('Patient added successfully', 'success')
    return redirect(url_for(patients))

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
    return render_template('./dashboard/reports.html')

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
