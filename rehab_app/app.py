from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify


app = Flask(__name__)

USERNAME = "admin"
STAFFPASSWORD = 'Password1234'

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
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")
        if new_password == confirm_password:
            # Update password logic (you may want to store it securely)
            STAFF_PASSWORD = new_password
            #session.pop("logged_in", None)
            return redirect(url_for("dashboard"))
        else:
            error_message = "Passwords do not match. Please try again."
            return render_template("change_password.html", error_message=error_message)
    return render_template("change_password.html")

@app.route('/dashboard')
def dashboard():
    #if not session.get("logged_in"):
     #   return redirect(url_for("login"))
    """Renders the dashboard.html template"""
    return render_template('./dashboard/dashboard.html')

# Sample data for demonstration purposes
patients = [
    {"id": 1, "name": "John Doe", "age": 30, "gender": "Male"},
    {"id": 2, "name": "Jane Smith", "age": 25, "gender": "Female"}
]

# Route for adding a new patient
@app.route('/add-patient', methods=['POST'])
def add_patient():
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    # Add the new patient to the list (for demonstration purposes)
    patients.append({"id": len(patients) + 1, "name": name, "age": age, "gender": gender})
    return redirect(url_for('dashboard'))

# Route for editing a patient
@app.route('/edit-patient/<int:patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    if request.method == 'POST':
        # Update the patient's information (for demonstration purposes)
        patients[patient_id - 1]['name'] = request.form.get('name')
        patients[patient_id - 1]['age'] = request.form.get('age')
        patients[patient_id - 1]['gender'] = request.form.get('gender')
        return redirect(url_for('dashboard'))
    else:
        # Render the edit patient form
        patient = patients[patient_id - 1]  # Subtract 1 because list indices start from 0
        return render_template('edit_patient.html', patient=patient)

# Route for deleting a patient
@app.route('/delete-patient/<int:patient_id>', methods=['POST'])
def delete_patient(patient_id):
    # Delete the patient from the list (for demonstration purposes)
    del patients[patient_id - 1]
    return redirect(url_for('dashboard'))

# Route for adding a new appointment
@app.route('/add-appointment', methods=['POST'])
def add_appointment():
    patient_id = int(request.form.get('patient'))
    date = request.form.get('date')
    time = request.form.get('time')
    # Add the new appointment to the list (for demonstration purposes)
    appointments.append({"id": len(appointments) + 1, "patient_id": patient_id, "patient_name": patients[patient_id - 1]['name'], "date": date, "time": time})
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    #session.pop("logged_in", None)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
