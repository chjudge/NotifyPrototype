from flask_wtf import FlaskForm
from wtforms.fields import (SubmitField, EmailField, TelField, StringField,
                            SelectField, TextAreaField)
from wtforms.validators import InputRequired, Email, EqualTo, Length

STATES = ['All', 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
          'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD',
          'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
          'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
          'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


class RegisterForm(FlaskForm):
    fname = StringField("First Name: ", validators=[InputRequired()])
    lname = StringField("Last Name: ", validators=[InputRequired()])
    email = EmailField("Email: ", validators=[
                       InputRequired(), Email('Email must be in valid format')])
    phone = TelField("Mobile Phone Number: ", validators=[
                     InputRequired(), Length(10)])
    state = SelectField("State: ", choices=STATES,
                        validators=[InputRequired()])
    county = SelectField('County:', choices=[
                         'County1', 'County2', 'County3', 'County4'], validators=[InputRequired()])
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
    state = SelectField('State:', choices=STATES, validators=[InputRequired()])
    county = SelectField('County:', choices=[
                         'All', 'County1', 'County2', 'County3', 'County4'], validators=[InputRequired()])
    precinct = SelectField('Precinct:', choices=[
                           'All', 'Precinct1', 'Precinct2', 'Precinct3', 'Precinct4'], validators=[InputRequired()])
    subject = StringField('Subject:', validators=[InputRequired()])
    message = TextAreaField("Message: ", validators=[InputRequired()])
    submit = SubmitField("Send")
