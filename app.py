from flask import Flask, render_template

from forms import RegisterForm

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY'] = 'bf228mslOG748F7lmfusbgru'

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/register/')
def get_register():
    r_form = RegisterForm()
    return render_template('register.html', form=r_form)

if __name__ == '__main__':
    app.run()
