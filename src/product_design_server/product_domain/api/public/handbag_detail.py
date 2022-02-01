from product_domain.models import HandbagDetail

def get_or_create_handbag_detail(name, url, description, meta, product):
    """
    External Interface for HandbagDetail.get_or_create()
    """
    handbag_detail = HandbagDetail.get_or_create(name, url, description, meta, product)
    return {
        'id': handbag_detail.id,
        'name': handbag_detail.name,
        'url': handbag_detail.url,
        'meta': handbag_detail.meta,
        'description': handbag_detail.description,
        'product_id': handbag_detail.product_id,
        'type': handbag_detail.type,
    }