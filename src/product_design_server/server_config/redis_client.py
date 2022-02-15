import redis

from server_config import REDIS


class RedisClient:
    SINGLETON_INSTANCE = None

    def __init__(self):
        self.db = REDIS['db']
        self.socket_timeout = REDIS['socket_timeout']

    def get_instance(self):
        if not RedisClient.SINGLETON_INSTANCE:
            RedisClient.SINGLETON_INSTANCE = redis.StrictRedis(
                host=REDIS['host'], port=REDIS['port'], db=REDIS['db'], socket_timeout=REDIS['socket_timeout']
            )

        return RedisClient.SINGLETON_INSTANCE
