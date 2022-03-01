# from storage_backend import registry as storage_registry


class BaseLayer:
    NAME = "base"
    PREFIX = "base"

    SUPPORTED_STORAGE_BACKENDS = ["redis"]

    def __init__(self):
        pass
        # self.redis_store = storage_registry.redis
        # self.redis_store.add_layer(self.NAME, self.PREFIX)

    def update(self, *args, **kwargs):
        _update = getattr(self, f"_update_{self.SUPPORTED_STORAGE_BACKENDS}")
        _update(*args, **kwargs)

    def load(self, records):
        _load = getattr(self, f"_load_{self.SUPPORTED_STORAGE_BACKENDS}")
        _load(records)

    def extract(self):
        pass

    def transform(self):
        pass

    def refresh_layer(self):
        pass
