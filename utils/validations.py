import re
from flask import jsonify, make_response

def validate_party_key_pair_values(request):
    """Validates key-value pairs of request dictionary body"""

    keys = ['name', 'hqAddress', 'logoUrl']
    errors = []
    for key in keys:
        if not key in request.json:
            errors.append(key)
    return errors

def validate_office_key_pair_values(request):
    """Validates key-value pairs of request dictionary body"""

    keys = ['type', 'name']
    errors = []
    for key in keys:
        if not key in request.json:
            errors.append(key)
    return errors

def validate_login_key_pair_values(request):
    """Validates key-value pairs of request dictionary body"""
    keys = ['email', 'password']
    errors=[]
    for key in keys:
        if not key in request.json:
            errors.append(key)
    return errors

def error(status, message):
    """Captures error messages"""
  
    return make_response(jsonify({
            "status": status,
            "message": message
        }), status)
