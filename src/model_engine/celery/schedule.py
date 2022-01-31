from celery.schedules import crontab
from model_engine.celery.app import app


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls refresh_eta every minute
    return 0
