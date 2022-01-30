from __future__ import absolute_import

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server_config.settings')

app = Celery('product_design_server')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_default_queue = "product_design_server_celery"
app.conf.task_acks_late = True
app.autodiscover_tasks()
