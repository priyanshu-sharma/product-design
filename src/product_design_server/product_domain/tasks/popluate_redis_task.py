from product_domain.api.public import handbag_detail_api
from server_config.celery import app
from server_config import RedisClient


@app.task(
    autoretry_for=(Exception,),
    retry_backoff=True,
    acks_late=True,
    queue="populate_redis_queue",
)
def populate_redis_task(handbag_detail_id):
    redis_client = RedisClient().get_instance()
    handbag_detail = handbag_detail_api.get_handbag_details(handbag_detail_id)
    redis_client.hmset(handbag_detail['name'], handbag_detail)
    return {"status": "success", "id": handbag_detail_id}
