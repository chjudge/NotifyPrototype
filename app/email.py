from app import app, mail
from flask_mail import Message

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_test_email(user):
    send_email('Test',app.config['ADMINS'][0], recipients=[user.email], text_body=f'Test{user.first_name}', html_body=f'Test{user.last_name}')