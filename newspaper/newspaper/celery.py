import os
from celery import Celery
from celery.schedules import crontab


# Настройки для асинхронного взаимодействия Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newspaper.settings')

app = Celery('newspaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'newsarticle.tasks.weekly_send_notify',
        'schedule': crontab(),
        'args': ()
    }
}
