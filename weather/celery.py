from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

app = Celery('weather')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


timezone = 'Europe/Kiev'

app = Celery(broker='redis://localhost:6379/7',
             include=['openweathermap.tasks'])

app.conf.update(
    CELERY_RESULT_BACKEND='redis://localhost:6379/7',
    CELERY_DEFAULT_QUEUE="openweathermapApp",
    CELERY_DEFAULT_EXCHANGE="openweathermapApp",
    CELERY_DEFAULT_EXCHANGE_TYPE="direct",
    CELERY_DEFAULT_ROUTING_KEY="openweathermapApp",
    CELERY_ACCEPT_CONTENT=['json', ],
    CELERYBEAT_SCHEDULER="django_celery_beat.schedulers.DatabaseScheduler"
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
