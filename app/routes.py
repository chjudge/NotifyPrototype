import re
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import RegisterForm
from app.models import User
from app.email import send_test_email
from app import db

@app.get('/')
def index():  # put application's code here
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
            print('user exists')
            flash('This email address is already registered.')
            return redirect(url_for('get_register'))
        user = User.query.filter_by(phone=r_form.phone.data).first()
        if user:
            print('user exists')
            flash('This phone number is already registered.')
            return redirect(url_for('get_register'))




        user = User(r_form.fname.data, r_form.lname.data, r_form.email.data, r_form.phone.data.strip().replace(' ', ''), r_form.state.data, r_form.county.data, r_form.zip.data, r_form.precinct.data, r_form.party.data, 1 if r_form.voter.data == 'Yes' else 0, r_form.interest.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('get_register'))
    else:
        exclude = r'[\'\[\]]'
        for field, error in r_form.errors.items():
            print(f"{field}: {str(error)}")
            flash(f"{re.sub(exclude, '', str(error))}")
        return redirect(url_for('get_register'))

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