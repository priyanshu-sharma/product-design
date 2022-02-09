from product_domain.api.public import product_api, handbag_detail_api
from server_config.celery import app


@app.task(
    autoretry_for=(Exception,), retry_backoff=True, acks_late=True, queue="product_creation_queue",
)
def product_creation_task(serialized_data):
    product_name = serialized_data.get("product_name", None)
    product_type = serialized_data.get("product_type", None)
    product_meta = serialized_data.get("product_meta", {})
    product_description = serialized_data.get("product_description", None)
    product_dict = product_api.get_or_create_product(product_name, product_type, product_meta, product_description)
    product_details = serialized_data.get("product_details", [])
    handbag_detail_list = []
    for product_detail in product_details:
        handbag_detail_dict = handbag_detail_api.get_or_create_handbag_detail(
            name=product_detail.get("name"),
            url=product_detail.get("url"),
            description=product_detail.get("description"),
            meta=product_detail.get("meta"),
            product=product_dict["product"],
        )
        handbag_detail_list.append(handbag_detail_dict)
    return {"status": "success"}
