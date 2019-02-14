from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.user import User
from utils.validations import *
from functools import wraps
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                jwt_refresh_token_required, get_jwt_identity, verify_jwt_in_request, get_jwt_claims, get_raw_jwt)
from utils.validations import validate_login_key_pair_values

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

class SignUp:

    @auth.route('/signup', methods=['POST'])
    def signup():
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

        user = User().create_user(firstName, lastName, otherName, email,
                                  phoneNumber, passportUrl, isAdmin, isCandidate, password)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": user
        }), 201)


class Login:
    @auth.route('/login', methods=['POST'])
    def login():
        errors = validate_login_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if email == "":
            return make_response(jsonify({
                "status": 400,
                "message": "email cannot be blank",
            }), 400)

        if password == "":
            return make_response(jsonify({
                "status": 400,
                "message": "password cannot be blank",
            }), 400)

        if not User().search(email):
            return make_response(jsonify({
                "status": 403,
                "message": "That email is not registered",
            }), 403)

        user = User().login(email, password)

        if user:
            access_token = create_access_token(identity=user[7])
            return make_response(jsonify({
                "status": 200,
                "data": [{
                    "token": access_token,
                    "user": {
                        "id": user[0],
                        "firstName": user[1],
                        "lastName": user[2],
                        "otherName": user[3],
                        "email":user[4],
                        "phoneNumber":user[5],
                        "passportUrl":user[6],
                        "isAdmin": user[7],
                        "isCandidate": user[8]
                    }
                }]
            }))
        return make_response(jsonify({"message": "wrong credentials"}), 401)
