from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    # Render the index.html template
    title = 'Rehab Center Management System'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def contact():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/resources')
def contact():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(debug=True)