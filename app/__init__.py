import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from sqlalchemy import inspect

app = Flask(__name__)

# Make sure this directory is in your Python path for imports
scriptdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scriptdir)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'bf228mslOG748F7lmfusbgru'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# for gmail mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = 1
app.config['MAIL_USERNAME'] = 'wplibertynotification'
app.config['MAIL_PASSWORD'] = 'pazzw0rd'
app.config['MAIL_DEFAULT_SENDER'] = 'wplibertynotification@gmail.com'

app.config['MAIL_SUPPRESS_SEND'] = False

# for localhost mail server
# app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
# app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT') or 25)
# app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') is not None
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['ADMINS'] = ['no-reply@site.com']

mail = Mail(app)

db = SQLAlchemy(app)


from app import routes
from app import email
from app import forms
from app import models

# check if users table exists
if(not inspect(db.engine).has_table('users')):
    db.create_all()
    print('table created')
