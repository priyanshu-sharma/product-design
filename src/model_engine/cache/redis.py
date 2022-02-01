from redis import Redis
from settings import storage_config

class Redis(object):
    def __init__(self, url):
        self.client = Redis.from_url(url)

    def save(self, key, record, expiry):
        self.client.set(key, record, expiry)

    def fetch(self, key):
        return self.client.get(key)

cache = Redis(storage_config["cache"])