from functools import wraps
from utils.validations import error
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    verify_jwt_in_request,
    get_jwt_claims,)


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_holder()
        if get_jwt_claims()['isAdmin'] != True:
            return error(403, "Admin rights required!")
            pass
        return fn(*args, **kwargs)
    return wrapper


def jwt_holder():
    return verify_jwt_in_request()


allowed_offices = ['Presidential', 'Gubernatorial', 'Senatorial',
                   'Member of County Assembly', 'Member of National Assembly', 'Women Representative']
allowed_office_types = ['National', 'County']
