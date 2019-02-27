import re
from flask import jsonify, make_response


def validate_party_key_pair_values(request):
    """Validates key-value pairs of request dictionary body"""

    keys = ['name', 'hqAddress', 'logoUrl']
    errors = []
    for key in keys:
        if key not in request.json:
            errors.append(key)
    return errors


def validate_office_key_pair_values(request):
    """Validates key-value pairs of request dictionary body"""

    keys = ['name', 'officeType']
    errors = []
    for key in keys:
        if key not in request.json:
            errors.append(key)
    return errors


def validate_login_key_pair_values(request):
    """Validates key-value pairs of request dictionary body"""
    keys = ['email', 'password']
    errors = []
    for key in keys:
        if key not in request.json:
            errors.append(key)
    return errors


def validate_user_key_pair_values(request):
    """Validates key-value pairs of request dictionary body"""

    keys = [
        'firstName',
        'lastName',
        'otherName',
        'email',
        'passportUrl',
        'password']
    errors = []
    for key in keys:
        if key not in request.json:
            errors.append(key)
    return errors


def error(status, message):
    """Captures error messages"""
    return make_response(jsonify({
        "status": status,
        "message": message
    }), status)


def response(status, message):
    """Captures success responses that do not return data"""
    return make_response(jsonify({
        "status": status,
        "message": message
    }), status)


def success(status, message, data):
    """Captures success messages"""
    return make_response(jsonify({
        "status": status,
        "message": message,
        "data": data
    }))


def validEmail(email):
    """Regex to validate email address"""
    if re.match(
        r"^[a-zA-Z0-9!#$&_*?^{}~-]+(\.[a-zA-Z0-9!#$&_*?^{}~-]+)*@([a-z0-9]+([a-z0-9-]*)\.)+[a-zA-Z]+$",
            email):
        return True


def validUrl(url):
    """Regex to validate image URLs"""
    if re.match(r"(http(s?):)|([/|.|\w|\s])*\.(?:jpg|gif|png|jpeg|img)", url):
        return True


def validPassword(password):
    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return True


def isBlank(variable):
    """check if variable is empty"""
    if variable == "":
        return True


def check_for_blanks(data):
    blanks = []
    for key, value in data.items():
        if value == "":
            blanks.append(key)
    return blanks


def check_for_non_strings(data):
    non_strings = []
    for key, value in data.items():
        if key != 'id' and not isinstance(value, str):

            non_strings.append(key)
    return non_strings


def check_for_non_ints(data):
    non_ints = []
    for key, value in data.items():
        if not isinstance(value, int):
            non_ints.append(key)
    return non_ints
