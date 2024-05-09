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

@app.route('/staff' , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get("password")
        if password == STAFFPASSWORD:
            return redirect(url_for('change_password'))
        else:
            error_message="Invalid password. Please try again!"
            return render_template("staff.html", error_message=error_message)
    """Renders the login.html template"""
    return render_template('staff.html')


if __name__ == '__main__':
    app.run(debug=True)
