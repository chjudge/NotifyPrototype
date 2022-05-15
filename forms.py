from typing import Text
from flask_wtf import FlaskForm
from wtforms.fields import (PasswordField, SubmitField, EmailField, TelField, StringField,
    SelectField, TelField, TextAreaField, IntegerField)
from wtforms.validators import InputRequired, Email, EqualTo, Length

STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
            'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD', 
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 
            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

class RegisterForm(FlaskForm):
    fname = StringField("First Name: ", validators=[InputRequired()])
    lname = StringField("Last Name: ", validators=[InputRequired()])
    email = EmailField("Email: ", validators=[InputRequired(), Email('Email must be in valid format')])
    number = TelField("Mobile Phone Number: ", validators=[InputRequired(), Length(10)])
    state = SelectField("State: ", choices=STATES)
    zip =  IntegerField("Zip Code: ", validators=[InputRequired(), Length(5)])
    # Precinct 
    submit = SubmitField("Register")