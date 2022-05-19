import re
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import RegisterForm, MessageForm
from app.models import Counties, User
from app.email import send_test_email, send_broadcast_email, send_verification_email
from app import db


@app.get('/')
def index():  # put application's code here
    return redirect(url_for('get_register'))


@app.get('/register/')
def get_register():
    r_form = RegisterForm()

    
# load data from text file into locations table
#     with open('app/static/data/pa_counties.txt', 'r') as f:
#         pa_counties = f.read().splitlines()
#         for county in pa_counties:
#             # add new entry to the locations table
#             db.session.add(Counties('Pennsylvania', county))
#         db.session.commit()
#         print('data loaded')
    
#     return render_template('register.html', form=r_form)


@app.post('/register/')
def post_register():
    r_form = RegisterForm()
    if r_form.validate():

        # check if user email or phone already exists
        user = User.query.filter_by(email=r_form.email.data).first()
        if user:
            print('user exists')
            flash('This email address is already registered.')
            return redirect(url_for('get_register'))
        user = User.query.filter_by(phone=r_form.phone.data).first()
        if user:
            print('user exists')
            flash('This phone number is already registered.')
            return redirect(url_for('get_register'))

        user = User(r_form.fname.data, r_form.lname.data, r_form.email.data, r_form.phone.data.strip().replace(' ', ''), r_form.state.data,
                    r_form.county.data, r_form.zip.data, r_form.precinct.data, r_form.party.data, 1 if r_form.voter.data == 'Yes' else 0, r_form.interest.data)
        db.session.add(user)
        db.session.commit()
        send_verification_email(user)
        return redirect(url_for('verify_email'))
    else:
        exclude = r'[\'\[\]]'
        for field, error in r_form.errors.items():
            print(f"{field}: {str(error)}")
            flash(f"{re.sub(exclude, '', str(error))}")
        return redirect(url_for('get_register'))


@app.get('/verify/')
@app.get('/verify/<token>')
def verify_email(token=None):
    if token is None:
        return render_template('verify.html')
    user = User.verify_token(token)
    if user is None:
        flash('This link is invalid or has expired.')
        return render_template('verify.html')
    user.verified_email = 1
    db.session.commit()
    flash('You have verified your email address!')
    return render_template('verify.html')


@app.get('/admin/')
def get_admin():
    users = User.query.all()
    return render_template('admin.html', users=users)


@app.post('/admin/')
def post_admin():
    if request.form.get('email_user') is not None:
        user_id = request.form.get('email_user')
        print(user_id)
        user = User.query.filter_by(id=user_id).first()
        if user:
            send_test_email(user)
            flash('Email sent to ' + user.email)
        else:
            flash('User not found')
        return redirect(url_for('get_admin'))
    return redirect(url_for('get_admin'))


@app.get('/message/')
def get_message():
    form = MessageForm()
    return render_template('message.html', form=form)

# send email to all users in the state, county, and precinct


@app.post('/message/')
def post_message():
    form = MessageForm()
    if form.validate():
        state = form.state.data
        county = form.county.data
        precinct = form.precinct.data
        validated = User.query.filter_by(verified_email=1)
        if(state == 'All'):
            users = validated.all()
        elif(county == 'All'):
            users = validated.filter_by(state=form.state.data).all()
        elif(precinct == 'All'):
            users = validated.filter_by(
                state=form.state.data, county=form.county.data).all()
        else:
            users = validated.filter_by(
                state=form.state.data, county=form.county.data, precinct=form.precinct.data).all()

        print(users)

        emails = list(map(lambda u: u.email, users))
        if emails:
            send_broadcast_email(
                emails=emails, subject=form.subject.data, body=form.message.data)
            flash('Email sent to all users in ' + form.state.data +
                  ', ' + form.county.data + ', ' + form.precinct.data)
        else:
            flash('No users found')
        return redirect(url_for('get_message'))
    else:
        exclude = r'[\'\[\]]'
        for field, error in form.errors.items():
            print(f"{field}: {str(error)}")
            flash(f"{re.sub(exclude, '', str(error))}")
        return redirect(url_for('get_message'))


@app.get('/api/counties/<state>')
def get_counties(state):
    counties = Locations.query.filter_by(state=state).all()
    counties = list(dict.fromkeys(counties))
    return {'counties': [c.county for c in counties]}