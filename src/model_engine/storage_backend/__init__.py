from model_engine.utils.singleton import Singleton
from model_engine.settings import storage_config
from model_engine.storage_backend.redis_store import RedisStore


class StorageBackendRegistry(metaclass=Singleton):
    def __init__(self):
        super(StorageBackendRegistry, self).__init__()
        self._redis = None

    @property
    def redis(self):
        if self._redis is None:
            self._redis = RedisStore(storage_config["redis"])
        return self._redis


registry = StorageBackendRegistry()


if __name__ == "__main__":
    r = registry.redis
