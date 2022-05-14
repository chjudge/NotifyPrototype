from flask import Flask, redirect, render_template, url_for

from forms import RegisterForm

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'bf228mslOG748F7lmfusbgru'

@app.get('/')
def hello_world():  # put application's code here
    return redirect(url_for('get_register'))

@app.get('/register/')
def get_register():
    r_form = RegisterForm()
    return render_template('register.html', form=r_form)

if __name__ == '__main__':
    app.run()
