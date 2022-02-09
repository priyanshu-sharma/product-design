# -*- coding: utf-8 -*-
from starlette.config import Config
import yaml
import os

# Config will be read from environment variables and/or ".env" files.

_env = Config(".env")

try:
    LOGGING_CONFIG_PATH = _env('LOGGING_CONFIG_PATH')
    env = os.environ.get('ENV', '')
    if env == 'test':
        with open(_env('TEST_CONFIG_PATH')) as f:
            config = yaml.safe_load(f)
    else:
        with open(_env('CONFIG_PATH')) as f:
            config = yaml.safe_load(f)
except ImportError:
    pass

celery_config = config["celery"]
storage_config = config["storage"]
database = config["database"]
generator_pickle = config['pickle_models']['generator']
generator = config['generator']
media = config['media']
fps = config['fps']