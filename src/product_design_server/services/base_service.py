import logging
import requests
from django.conf import settings
from extensions.exceptions import NetworkException, ResourceConflictException, \
    ResourceNotFoundException, BadRequestException, ParseException
from extensions.utilities import is_success, is_client_error

logger = logging.getLogger(__name__)


class BaseService(object):

    def __init__(self, host, is_logging_enabled=False):
        self.host = host.rstrip('/')
        self.host += '/'
        self.is_logging_enabled = is_logging_enabled

    def get_data_from_client_response(self, response, method):
        if method == 'HEAD':
            return response

        if is_success(response.status_code):
            if response.status_code == requests.codes.no_content:
                return {}

            if self.is_logging_enabled:
                logger.debug('Success Response: {}'.format(response.text))
            return response.json()

        message = response.text
        logger.debug('Failure Response: {}'.format(message))

        logger_message = response.url + ' ' + message

        # map response to corresponding exceptions

        if response.status_code == requests.codes.bad_request:
            raise BadRequestException(logger_message)
        if response.status_code == requests.codes.not_found:
            raise ResourceNotFoundException(logger_message)
        if response.status_code == requests.codes.conflict:
            raise ResourceConflictException(logger_message)
        if is_client_error(response.status_code):
            raise ParseException(logger_message)

        raise NetworkException(logger_message)

    def request(self, method, relative_url, data=None, params=None, headers=None, auth=None,
                timeout_seconds=settings.DEFAULT_TIMEOUT_SECONDS):
        request_url = self.host + relative_url.lstrip('/')
        try:
            response = requests.request(method=method, url=request_url, json=data, params=params, headers=headers,
                                        auth=auth, timeout=timeout_seconds)

        except Exception as e:
            raise NetworkException() from e
        return self.get_data_from_client_response(response, method)

    def head(self, relative_url, params=None, headers=None, auth=None,
             timeout_seconds=settings.DEFAULT_TIMEOUT_SECONDS):
        return self.request('HEAD', relative_url, data=None, params=params, headers=headers,
                            timeout_seconds=timeout_seconds, auth=auth)

    def get(self, relative_url, params=None, headers=None, auth=None, timeout_seconds=settings.DEFAULT_TIMEOUT_SECONDS):
        return self.request('GET', relative_url, data=None, params=params, headers=headers,
                            timeout_seconds=timeout_seconds, auth=auth)

    def post(self, relative_url, data=None, params=None, headers=None, auth=None,
             timeout_seconds=settings.DEFAULT_TIMEOUT_SECONDS):
        return self.request('POST', relative_url, data=data, params=params, headers=headers, auth=auth,
                            timeout_seconds=timeout_seconds)

    def put(self, relative_url, data=None, params=None, headers=None, auth=None,
            timeout_seconds=settings.DEFAULT_TIMEOUT_SECONDS):
        return self.request('PUT', relative_url, data=data, params=params, headers=headers, auth=auth,
                            timeout_seconds=timeout_seconds)

    def patch(self, relative_url, data=None, params=None, headers=None, auth=None,
              timeout_seconds=settings.DEFAULT_TIMEOUT_SECONDS):
        return self.request('PATCH', relative_url, data=data, params=params, headers=headers, auth=auth,
                            timeout_seconds=timeout_seconds)

    def delete(self, relative_url, params=None, headers=None, auth=None,
               timeout_seconds=settings.DEFAULT_TIMEOUT_SECONDS):
        return self.request('DELETE', relative_url, data=None, params=params, headers=headers, auth=auth,
                            timeout_seconds=timeout_seconds)
