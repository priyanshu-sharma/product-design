from celery import Celery
from server_config import celery_config


app = Celery()
app.conf.broker_url = celery_config["broker_url"]

# TODO use a callable to discover tasks based on a convention.
app.autodiscover_tasks(["model_engine.async_celery.schedule", "model_engine.async_celery.tasks"])
