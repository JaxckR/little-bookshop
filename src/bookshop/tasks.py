from django.core.mail import send_mail

from config.celery import app
from config.settings import EMAIL_HOST_USER


@app.task
def send_user_email(user_email):
    send_mail('This is a spam email',
              'This is a spam email again but its message not subject',
              EMAIL_HOST_USER,
              [user_email])

@app.task
def send_me_msg():
    send_mail('this is no spam email',
              'im believe that you thrust me',
              EMAIL_HOST_USER,
              ['winelkon@gmail.com'])