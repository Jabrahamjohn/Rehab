#!/usr/bin/env python3
import uuid

from flask import render_template, request, redirect, url_for, flash, session, jsonify
from models import app, Treatment_Plan, Progress, Medication, Patient, Therapist, Appointment
from models import db #mysql


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

@app.route('/privacystatement')
def privacystatement():
    """Renders the privacystatement.html template."""
    return render_template('privacystatement.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the request method is not 'POST', render the login form template
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        if email == 'rehab@gmail.com':
            id = str(uuid.uuid4())
            session['id'] = id
            session['password'] = password
            return redirect(url_for('dashboard', id=id))
        else:
            error = 'Invalid username/password'
            return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/dashboard/<id>')
def dashboard(id):
    user_id = id
    print("Dashboard id:", user_id)
    role = session.get('role')
    return render_template('admin-ui/dashboard.html', id=user_id, role=role)
    
@app.route('/patients/<id>')
def patients(id):
    user_id = session.get('id')
    role = session.get('role')
    return render_template('admin-ui/patients.html', id=user_id, role=role)


@app.route('/staff/<id>')
def staff(id):
    """Renders the appointments.html template"""
    user_id = session.get('id')
    role = session.get('role')
    return render_template('./admin-ui/staff.html', id=user_id, role=role)

@app.route('/resources/<id>')
def resourcs(id):
    """Renders the resources.html template"""
    user_id = session.get('id')
    print(user_id)
    role = session.get('role')
    return render_template('./admin-ui/resources.html', id=user_id, role=role)


if __name__ == '__main__':
    app.secret_key = 'AJ'
    app.run(debug=True)
