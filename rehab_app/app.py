#!/usr/bin/env python3

from flask import render_template, request, redirect, url_for, flash, session, jsonify
from models import app, Treatment_Plan, Progress, Medication, Patient, Therapist, Appointment
from models import db, mysql, login_manager, User
from werkzeug.security import generate_password_hash
from flask_login import login_required
from werkzeug.security import check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    #Create all the db models into the database
    if not User.query.filter_by(username='admin').first():
        hashed_password = generate_password_hash('admin', method='sha256')
        new_user = User(name='Admin User', username='admin', phone_number='1234567890', email='admin@example.com', role='admin', password=hashed_password)
        db.session.add(new_user)
        db.session.commit()


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            if user.password == generate_password_hash('admin', method='sha256'):  # Check if default password
                return redirect(url_for('change_password'))
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('login.html')

@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        if new_password == confirm_password:
            hashed_password = generate_password_hash(new_password, method='sha256')
            current_user.password = hashed_password
            db.session.commit()
            flash('Your password has been updated!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Passwords do not match!', 'danger')
    
    return render_template('change_password.html')

@app.route('/dashboard')
def dashboard():
    # Check if the 'username' key exists in the session
    if 'username' in session:
        # User is logged in, render the dashboard
        return render_template('./dashboard/dashboard.html')
    else:
        # User is not logged in, redirect to the login page
        flash('You need to login first.', 'error')
        return redirect(url_for('login'))
    
@app.route('/patients')
def patients():
    """Renders the patients.html template"""
    patients = Patient.query.all()
    return render_template('./dashboard/patients.html', patients=patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    try:
        name = request.form['name']
        year = request.form['year']  # Change from 'age' to 'year' to match the model
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        email = request.form['email']
        medical_history = request.form['medical_history']
        treatment_plan_id = request.form['treatment_plan']  # Assuming treatment_plan_id is provided
        medication_plan_id = request.form['medication_plan']  # Assuming medication_plan_id is provided
        progress_notes = request.form['progress_notes']
    # Create a new Patient instance
        new_patient = Patient(
            name=name,
            year=year,
            gender=gender,
            phone_number=phone_number,
            email=email,
            medical_history=medical_history,
            treatment_plan=treatment_plan_id,
            medication_plan=medication_plan_id,
            progress_notes=progress_notes
        )

        # Add the new patient to the database
        db.session.add(new_patient)
        db.session.commit()

        flash('Patient added successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash('An error occured.')
    finally:
        db.session.close()
    return redirect(url_for('patients'))

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
    return render_template('./dashboard/medication.html')

@app.route('/reports')
def reports():
    """Renders the reports.html template"""
    return render_template('./dashboard/users.html')

@app.route('/tasks')
def tasks():
    """Renders the tasks.html template"""
    return render_template('./dashboard/progress.html')

@app.route('/logout')
def logout():
    session.pop("username", None)  # Clear the session variable
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.secret_key = 'AJ'
    app.run(debug=True)
