class BaseServiceError(Exception):
    code = 500
    message = 'Unexpected error'


class ItemNotFound(BaseServiceError):
    code = 404
    message = 'Not Found'


class UserAlreadyExists(BaseServiceError):
    code = 400
    message = 'user exists'
