from redis import Redis
from extensions import chunkify, Singleton
from storage_backend.base import BaseStorageBackend


class RedisStore(BaseStorageBackend, metaclass=Singleton):
    def __init__(self, url, default_batchsize=1000):
        super().__init__()
        self.socket_timeout = 0.5
        self.client = Redis.from_url(url, socket_timeout=self.socket_timeout)
        self.default_batchsize = default_batchsize

    @property
    def layer_prefixes(self):
        return self.client.hgetall("layer_prefixes")

    def _upsert_layer(self, name, prefix):
        return self.client.hset("layer_prefixes", name, prefix)

    def add_layer(self, name, prefix, if_exists="ignore"):
        prefixes = self.layer_prefixes
        if name in prefixes:
            if if_exists == "ignore":
                return
            elif if_exists == "raise":
                raise Exception(f"Layer:{name} exists with prefix:{prefix}")
            elif if_exists == "replace":
                self._upsert_layer(name, prefix)
                return
        else:
            self._upsert_layer(name, prefix)
