from flask_wtf import FlaskForm
from wtforms.fields import (SubmitField, EmailField, TelField, StringField,
                            SelectField, TextAreaField)
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(FlaskForm):
    with open('app/static/data/states.txt') as f:
        states = f.read().splitlines()
        states = [('All', 'All')] + [(state.strip(), state.strip()) for state in states]
    fname = StringField("First Name: ", validators=[InputRequired()])
    lname = StringField("Last Name: ", validators=[InputRequired()])
    email = EmailField("Email: ", validators=[
                       InputRequired(), Email('Email must be in valid format')])
    phone = TelField("Mobile Phone Number: ", validators=[
                     InputRequired(), Length(10)])
    state = SelectField("State: ", choices=states,
                        validators=[InputRequired()])
    county = SelectField('County:', choices=['Please select a state'], validators=[InputRequired()], validate_choice=False)
    zip = StringField("Zip Code: ", validators=[InputRequired(), Length(5)])
    precinct = SelectField('Precinct:', choices=[
                           'Precinct1', 'Precinct2', 'Precinct3', 'Precinct4'], validators=[InputRequired()])
    party = SelectField('Party Affiliation:', choices=[
                        'Democrat', 'Republican', 'Other'], validators=[InputRequired()])
    voter = SelectField('Are you registered to vote?', choices=[
                        'Yes', 'No'], validators=[InputRequired()])
    interest = SelectField('Are you interested in becoming a:', choices=[
                           'Neither', 'County Leader', 'Both', 'Precinct Leader'], validators=[InputRequired()])
    submit = SubmitField("Register")

# select state, county, and precinct to send email


class MessageForm(FlaskForm):
    with open('app/static/data/states.txt') as f:
        states = f.read().splitlines()
        states = ['All'] + [state.strip() for state in states]
    state = SelectField('State:', choices=states, validators=[InputRequired()])
    county = SelectField('County:', choices=[
                         'All'], validators=[InputRequired()])
    precinct = SelectField('Precinct:', choices=[
                           'All', 'Precinct1', 'Precinct2', 'Precinct3', 'Precinct4'], validators=[InputRequired()])
    subject = StringField('Subject:', validators=[InputRequired()])
    message = TextAreaField("Message: ", validators=[InputRequired()])
    submit = SubmitField("Send")
