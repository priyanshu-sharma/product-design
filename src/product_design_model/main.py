from fastapi import FastAPI
from marshmallow.exceptions import ValidationError

from server_config import BASE_DIR

import logging

logging.config.fileConfig(BASE_DIR + '/server_config/logging.conf', disable_existing_loggers=False)

from extensions import (
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
    SchemaExceptionHandler,
)

app = FastAPI(title="Product Design Model API")


@app.get("/health_check")
def health():
    return {'health': 'ok'}


app.add_exception_handler(NetworkException, NetworkExceptionHandler)
app.add_exception_handler(ResourceConflictException, ResourceConflictExceptionHandler)
app.add_exception_handler(ResourceNotFoundException, ResourceNotFoundExceptionHandler)
app.add_exception_handler(BadRequestException, BadRequestExceptionHandler)
app.add_exception_handler(ParseException, ParseExceptionHandler)
app.add_exception_handler(ValidationError, SchemaExceptionHandler)