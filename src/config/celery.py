import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send_spam_every_5_min': {
        'task': 'bookshop.tasks.send_me_msg',
        'schedule': crontab(minute='*/5')
    }
}