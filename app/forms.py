from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError

class ContactForm(FlaskForm):
    name = StringField("User Name", [DataRequired(message="Enter Name here")])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    address = TextAreaField("Address")
    email = StringField("Email", [DataRequired(message="Enter Email here"), Email(message="Enter a valid email address")])
    age = IntegerField("Age")
    language = SelectField('Language', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Submit")
