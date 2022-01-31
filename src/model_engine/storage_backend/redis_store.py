from model_engine.storage_backend.base import BaseStorageBackend
import redis
from model_engine.utils import chunkify
from model_engine.utils.singleton import Singleton


class LayerExists(Exception):
    pass


class RedisStore(BaseStorageBackend, metaclass=Singleton):
    def __init__(self, url, default_batchsize=1000):
        super().__init__()
        self.socket_timeout = 0.5
        # self.client = redis.Redis.from_url(url, socket_timeout=self.socket_timeout)
        self.client = redis.Redis.from_url(url)
        self.default_batchsize = default_batchsize