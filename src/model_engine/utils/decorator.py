import time
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


def log_runtime_duration(foo):
    def bar(*args, **kwargs):
        start = time.time()
        foo(*args, **kwargs)
        logger.info(
            f"{foo.__qualname__} :: start_time: {start}, end_time: {time.time()}, duration: {time.time() - start}"
        )

    return bar
