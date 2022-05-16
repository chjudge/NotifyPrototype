from distutils.command.config import config
from app import app, mail
from flask_mail import Message


def send_test_email(user):
    msg = Message(subject='Test', recipients=[user.email])
    msg.body = f'Test{user.first_name}'
    # msg.html = f'Test{user.last_name}'
    mail.send(msg)


def send_broadcast_email(emails, subject, body):
    msg = Message(subject=subject, recipients=[
                  app.config['MAIL_DEFAULT_SENDER']], bcc=emails)
    print(f'sending email to {msg.bcc[0]}')
    msg.body = body
    # msg.html = f'Test{user.last_name}'
    mail.send(msg)
