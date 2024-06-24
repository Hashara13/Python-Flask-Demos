from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    pin = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for displaying the form
@app.route('/')
def index():
    return render_template('form.html')

# Route for handling form submissions
@app.route('/addrec', methods=['POST'])
def addrec():
    name = request.form['nm']
    address = request.form['add']
    city = request.form['city']
    pin = request.form['pin']

    new_student = Student(name=name, address=address, city=city, pin=pin)
    db.session.add(new_student)
    db.session.commit()

    return redirect(url_for('show_all'))

# Route for displaying all records
@app.route('/show_all')
def show_all():
    students = Student.query.all()
    return render_template('show_all.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
