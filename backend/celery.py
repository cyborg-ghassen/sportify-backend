from __future__ import absolute_import

import os
import subprocess

from celery import Celery, shared_task
from celery.schedules import crontab
from django.conf import settings
from datetime import timedelta

from django.utils.module_loading import import_string

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
app = Celery('backend')
app.conf.enable_utc = False
app.conf.update(timezone='Africa/Tunis')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
