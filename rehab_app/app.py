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
            return redirect(url_for('change_password'))
        else:
            error_message="Invalid password. Please try again!"
            return render_template("login.html", error_message=error_message)
    """Renders the login.html template"""
    return render_template('login.html')
@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if password == confirm_password:
            STAFFPASSWORD = password
            return redirect(url_for('dashboard'))
        else:
            error_message="Passwords do not match. Please try again!"
            return render_template("change_password.html", error_message=error_message)
    """Renders the change_password.html template"""
    return render_template('change_password.html')

@app.route('/dashboard')
def dashboard():
    """Renders the dashboard.html template"""
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
