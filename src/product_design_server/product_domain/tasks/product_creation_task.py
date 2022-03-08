from product_domain.api.public import product_api, handbag_detail_api
from server_config.celery import app
import pickle
from django.db import transaction

def redis_refresh(handbag_detail_list):
    from server_config import RedisClient
    redis_client = RedisClient().get_instance()
    for key in redis_client.scan_iter("ip_*"):
        redis_client.delete(key)
    for handbag_details in handbag_detail_list:
        pickled_handbag_details = pickle.dumps(handbag_details)
        redis_client.set("ip_{}".format(handbag_details['name']), pickled_handbag_details)
    return {"status": "success", "message": "Redis refreshed"}

def database_refesh(serialized_data):
    product_name = serialized_data.get("product_name", None)
    product_type = serialized_data.get("product_type", None)
    product_meta = serialized_data.get("product_meta", {})
    product_description = serialized_data.get("product_description", None)
    product_dict = product_api.get_or_create_product(product_name, product_type, product_meta, product_description)
    product_details = serialized_data.get("product_details", [])
    handbag_detail_list = []
    for product_detail in product_details:
        handbag_detail_dict = handbag_detail_api.create_handbag_detail(
            name=product_detail.get("name"),
            url=product_detail.get("url"),
            description=product_detail.get("description"),
            meta=product_detail.get("meta"),
            product=product_dict["product"],
        )
        handbag_detail_list.append(handbag_detail_dict)
    return handbag_detail_list


@app.task(
    autoretry_for=(Exception,), retry_backoff=True, acks_late=True, queue="product_creation_queue",
)
def product_creation_task(serialized_data):
    with transaction.atomic():
        handbag_detail_list = database_refesh(serialized_data)
        redis_response = redis_refresh(handbag_detail_list)
        return redis_response
