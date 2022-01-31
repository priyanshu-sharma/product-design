from fastapi import Request
from fastapi.responses import JSONResponse
from marshmallow.exceptions import ValidationError


class NetworkException(Exception):
    def __init__(self, message: str):
        self.message = message


class ResourceConflictException(Exception):
    def __init__(self, message: str):
        self.message = message


class ResourceNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message


class BadRequestException(Exception):
    def __init__(self, message: str):
        self.message = message


class ParseException(Exception):
    def __init__(self, message: str):
        self.message = message


async def NetworkExceptionHandler(request: Request, exception: NetworkException):
    return JSONResponse(status_code=500, content={"message": str(exception.message)})


async def ResourceConflictExceptionHandler(request: Request, exception: ResourceConflictException):
    return JSONResponse(
        status_code=409,
        content={"message": "Record already exists. " + str(exception.message)},
    )


async def ResourceNotFoundExceptionHandler(request: Request, exception: ResourceNotFoundException):
    return JSONResponse(status_code=404, content={"message": str(exception.message)})


async def BadRequestExceptionHandler(request: Request, exception: BadRequestException):
    return JSONResponse(
        status_code=400,
        content={"message": "Invalid Input - " + str(exception.message)},
    )


async def ParseExceptionHandler(request: Request, exception: ParseException):
    return JSONResponse(status_code=400, content={"message": "Parse Error - " + str(exception.message)})


async def SchemaExceptionHandler(request: Request, exception: ValidationError):
    return JSONResponse(status_code=400, content={"message": "Schema Error - " + str(exception)})
