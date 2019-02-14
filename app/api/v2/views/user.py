from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.user import User
from utils.validations import *
from functools import wraps
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, verify_jwt_in_request, get_jwt_claims, get_raw_jwt)


auth = Blueprint('auth', __name__, url_prefix='/api/v2/auth')

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_holder()
        if get_jwt_claims()['isAdmin'] != True:
            return make_response(jsonify({"message": "Admin rights required!"}), 201)
            pass
        return fn(*args, **kwargs)
    return wrapper

def candidate_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_holder()
        if get_jwt_claims()['isCandidate'] != True:
            return make_response(jsonify({"message": "Candidate rights required!"}), 201)
            pass
        return fn(*args, **kwargs)
    return wrapper

class SignUp:

    @auth.route('/signup', methods=['POST'])

    def post_user():
        data = request.get_json()
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        otherName = data.get('otherName')
        email = data.get('email')
        phoneNumber = data.get('phoneNumber')
        passportUrl = data.get('passportUrl')
        isAdmin = data.get('isAdmin')
        isCandidate = data.get('isCandidate')
        password = data.get('password')

        user = User().create_user(firstName, lastName, otherName, email, phoneNumber, passportUrl, isAdmin, isCandidate, password)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": user
        }), 201)