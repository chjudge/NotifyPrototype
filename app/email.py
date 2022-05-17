from distutils.command.config import config
from app import app, mail
from flask_mail import Message
from threading import Thread
from flask import url_for


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_test_email(user):
    msg = Message(subject='Test', recipients=[user.email])
    msg.body = f'Test{user.first_name}'
    # msg.html =
    Thread(target=send_async_email, args=(app, msg)).start()


def send_verification_email(user):
    token = user.get_verification_token()
    msg = Message(subject='Email Verification', recipients=[user.email])
    msg.body = f'Hello {user.email}, \n\nPlease verify your email by clicking the link below:\n' + \
        url_for('verify_email', token=token, _external=True)
    Thread(target=send_async_email, args=(app, msg)).start()


def send_broadcast_email(emails, subject, body):
    msg = Message(subject=subject, recipients=[
                  app.config['MAIL_DEFAULT_SENDER']], bcc=emails)
    print(f'sending email to {msg.bcc[0]}')
    msg.body = body
    # msg.html =
    Thread(target=send_async_email, args=(app, msg)).start()
