from product_domain.models import HandbagDetail

def get_or_create_handbag_detail(name, url, description, metadata, product):
    """
    External Interface for HandbagDetail.get_or_create()
    """
    handbag_detail = HandbagDetail.get_or_create(name, url, description, metadata, product)
    return {
        'id': handbag_detail.id,
        'name': handbag_detail.name,
        'url': handbag_detail.url,
        'metadata': handbag_detail.metadata,
        'description': handbag_detail.description,
        'product_id': handbag_detail.product_id,
        'type': handbag_detail.type,
    }