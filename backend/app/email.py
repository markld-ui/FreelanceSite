# Other modules
from threading import Thread

# Flask modules
from flask import current_app
from flask_mail import Message

# Package modeules
from app import mail


def send_async_email(app, msg) -> None:
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body) -> None:
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()
