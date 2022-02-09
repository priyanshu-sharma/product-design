from redis import Redis
from extensions import chunkify, Singleton
from storage_backend.base import BaseStorageBackend


class RedisStore(BaseStorageBackend, metaclass=Singleton):
    def __init__(self, url, default_batchsize=1000):
        super().__init__()
        self.socket_timeout = 0.5
        # self.client = Redis.from_url(url, socket_timeout=self.socket_timeout)
        self.client = Redis.from_url(url)
        self.default_batchsize = default_batchsize
