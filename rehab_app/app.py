from flask import Flask, render_template, request, redirect, url_for, flash, session


app = Flask(__name__)

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
        password = request.form.get("password")
        if password == STAFFPASSWORD:
            #session["logged_in"] = True
            return redirect(url_for('change_password'))
        else:
            error_message="Invalid password. Please try again!"
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
"""
@app.route("/add-patient", methods=["POST"])
def add_patient():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    # Add patient to the list (for demonstration purposes)
    patients.append({"name": name, "age": age, "gender": gender})
    return redirect(url_for("dashboard"))
"""
# app.py

@app.route("/patient/<int:patient_id>")
def patient_details(patient_id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    # Retrieve patient details based on the patient_id (for demonstration purposes)
    patient = patients[patient_id - 1]  # Subtract 1 because list indices start from 0
    return render_template("patient_details.html", patient=patient)


if __name__ == '__main__':
    app.run(debug=True)
