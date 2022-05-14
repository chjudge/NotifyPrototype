from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, SubmitField, EmailField, TelField, StringField, SelectField
from wtforms.validators import InputRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    email = EmailField("Email: ", validators=[InputRequired(), Email('Email must be in valid format')])
    submit = SubmitField("Register")