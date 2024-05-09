from flask import Flask, render_template, request, redirect, url_for, flash, session


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
    return render_template('dashboard.html')

# Dummy data for demonstration
patients = [
    {"id": 1, "name": "John Doe", "age": 35, "gender": "Male"},
    {"id": 2, "name": "Jane Smith", "age": 28, "gender": "Female"},
    {"id": 3, "name": "Alice Johnson", "age": 45, "gender": "Female"}
]

# Route for adding a new patient
@app.route('/add_patient', methods=['POST'])
def add_patient():
    # Get form data
    name = request.form.get('name')
    age = int(request.form.get('age'))
    gender = request.form.get('gender')
    
    # Generate patient ID (for demonstration purposes)
    new_patient_id = len(patients) + 1
    
    # Add new patient to the list
    new_patient = {"id": new_patient_id, "name": name, "age": age, "gender": gender}
    patients.append(new_patient)
    
    # Redirect back to the dashboard
    return redirect(url_for('dashboard'))

# Route for viewing patients
@app.route('/patients')
def view_patients():
    return render_template('patients.html', patients=patients)

# Route for editing a patient
@app.route('/edit_patient/<int:patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    # Find the patient in the list by ID
    patient = next((p for p in patients if p['id'] == patient_id), None)
    if not patient:
        return 'Patient not found', 404
    
    if request.method == 'POST':
        # Update patient information with data from the form
        patient['name'] = request.form.get('name')
        patient['age'] = int(request.form.get('age'))
        patient['gender'] = request.form.get('gender')
        # Redirect back to the dashboard
        return redirect(url_for('dashboard'))
    
    # Render the edit patient form with the patient's current information
    return render_template('edit_patient.html', patient=patient)

@app.route('/logout')
def logout():
    #session.pop("logged_in", None)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
