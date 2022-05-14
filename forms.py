from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, SubmitField, StringField, SelectField
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import InputRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    email = EmailField("Email: ", validators=[InputRequired(), Email('Email must be in valid format')])
    password = PasswordField("Password: ", 
        validators=[InputRequired(), Length(min=8, max=256)])
    confirm_password = PasswordField("Confirm Password: ", 
        validators=[EqualTo('password', message='Passwords must match')])
    submit = SubmitField("Register")