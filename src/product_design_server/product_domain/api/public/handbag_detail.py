from product_domain.models import HandbagDetail


def create_handbag_detail(name, url, description, meta, product):
    """
    External Interface for HandbagDetail.create()
    """
    handbag_detail = HandbagDetail.create(name, url, description, meta, product)
    return {
        'id': handbag_detail.id,
        'name': handbag_detail.name,
        'url': handbag_detail.url,
        'meta': handbag_detail.meta,
        'description': handbag_detail.description,
        'product_id': handbag_detail.product_id,
        'type': handbag_detail.type,
        'active': handbag_detail.active,
    }


def get_handbag_details(id):
    """
    External Interface for HandbagDetail.get_or_create()
    """
    handbag_detail = HandbagDetail.get_handbag_details(id)
    return {
        'id': handbag_detail.id,
        'name': handbag_detail.name,
        'url': handbag_detail.url,
        'product_id': handbag_detail.product_id,
        'type': handbag_detail.type,
        'product_name': handbag_detail.product.name,
        'product_type': handbag_detail.product.type,
    }


def disable_handbag_details():
    """
    External Interface for HandbagDetail.disable_older_handbag_details()
    """
    HandbagDetail.disable_older_handbag_details()
    return {
        'message': 'Handbag details disabled successfully.'
    }