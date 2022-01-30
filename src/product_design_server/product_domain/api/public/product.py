from product_domain.models import Product

def get_or_create_product(name, type, metadata, description):
    """
    External Interface for Product.get_or_create()
    """
    product = Product.get_or_create(name=name, type=type, metadata=metadata, description=description)
    return {
        'id': product.id,
        'name': product.name,
        'type': product.type,
        'metadata': product.metadata,
        'description': product.description,
    }
