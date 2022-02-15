from product_domain.models import Product


def get_or_create_product(name, type, meta, description):
    """
    External Interface for Product.get_or_create()
    """
    product = Product.get_or_create(name=name, type=type, meta=meta, description=description)
    return {
        'id': product.id,
        'name': product.name,
        'type': product.type,
        'meta': product.meta,
        'description': product.description,
        'product': product,
    }
