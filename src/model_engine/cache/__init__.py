from model_engine.cache.redis import Redis
from model_engine.settings import storage_config

cache = Redis(storage_config["cache"])
