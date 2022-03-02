from product_domain.api.public import handbag_detail_api
from server_config.celery import app
from server_config import RedisClient


@app.task(
    autoretry_for=(Exception,), retry_backoff=True, acks_late=True, queue="populate_redis_queue",
)
def populate_redis_task(handbag_details):
    import pickle
    redis_client = RedisClient().get_instance()
    for handbag_detail in handbag_details:
        handbag_detail = handbag_detail_api.get_handbag_details(handbag_detail['id'])
        pickled_handbag_detail = pickle.dumps(handbag_detail)
        redis_client.set('ip_{}'.format(handbag_detail['name']), pickled_handbag_detail)
    return {"status": "success", "message": "Handbag details populated successfully"}
