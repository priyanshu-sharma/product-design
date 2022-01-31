import logging
import logging.config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from model_engine.api.router import api_router
from model_engine.settings import LOGGING_CONFIG_PATH
from model_engine.api import (
    NetworkException,
    NetworkExceptionHandler,
    ResourceConflictException,
    ResourceConflictExceptionHandler,
    ResourceNotFoundException,
    ResourceNotFoundExceptionHandler,
    BadRequestException,
    BadRequestExceptionHandler,
    ParseException,
    ParseExceptionHandler,
)


from model_engine.settings import LOGGING_CONFIG_PATH
from model_engine.server_config.database import Base, SQLALCHEMY_DATABASE_URL

logging.config.fileConfig(LOGGING_CONFIG_PATH, disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI(title="Product Design Model API", version="0.1")

app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    logger.info("Starting up Model Server")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Shut Down")


app.add_exception_handler(NetworkException, NetworkExceptionHandler)
app.add_exception_handler(ResourceConflictException, ResourceConflictExceptionHandler)
app.add_exception_handler(ResourceNotFoundException, ResourceNotFoundExceptionHandler)
app.add_exception_handler(BadRequestException, BadRequestExceptionHandler)
app.add_exception_handler(ParseException, ParseExceptionHandler)

