import sys, os
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import RegisterForm

# Make sure this directory is in your Python path for imports
scriptdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scriptdir)



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'bf228mslOG748F7lmfusbgru'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/flask_app'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), unique=False)
    last_name = db.Column(db.String(40), unique=False)
    email = db.Column(db.String(120), unique=False)
    phone = db.Column(db.String(10), unique=False)
    state = db.Column(db.String(40), unique=False)
    county = db.Column(db.String(40), unique=False)
    zipcode = db.Column(db.String(40), unique=False)
    precinct = db.Column(db.String(40), unique=False)
    party = db.Column(db.String(40), unique=False)
    voter = db.Column(db.Boolean, unique=False)
    interest = db.Column(db.String(40), unique=False)

    def __init__(self, first_name, last_name, email, phone, state, county, zipcode, precinct, party, voter, interest):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.state = state
        self.county = county
        self.zipcode = zipcode
        self.precinct = precinct
        self.party = party
        self.voter = voter
        self.interest = interest

@app.get('/')
def hello_world():  # put application's code here
    return redirect(url_for('get_register'))

@app.get('/register/')
def get_register():
    r_form = RegisterForm()
    return render_template('register.html', form=r_form)

@app.post('/register/')
def post_register():
    r_form = RegisterForm()
    if r_form.validate():

        # check if user email or phone already exists
        user = User.query.filter_by(email=r_form.email.data).first()
        if user:
            return redirect(url_for('get_register'))
        user = User.query.filter_by(phone=r_form.phone.data).first()
        if user:
            return redirect(url_for('get_register'))




        user = User(r_form.fname.data, r_form.lname.data, r_form.email.data, r_form.phone.data, r_form.state.data, r_form.county.data, r_form.zipcode.data, r_form.precinct.data, r_form.party.data, r_form.voter.data, r_form.interest.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('get_register'))
    else:
        return render_template('register.html', form=r_form)

if __name__ == '__main__':
    app.run()
