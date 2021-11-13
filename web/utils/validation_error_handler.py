import functools

from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest


def validation_error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            raise BadRequest(description=e.messages)

    return wrapper
