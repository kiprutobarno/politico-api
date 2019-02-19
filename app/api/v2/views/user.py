from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.user import User
from utils.validations import *
from functools import wraps
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                jwt_refresh_token_required, get_jwt_identity, verify_jwt_in_request, get_jwt_claims, get_raw_jwt)
from utils.validations import validate_login_key_pair_values

auth = Blueprint('auth', __name__)



class SignUp:
    """User signup endpoint"""
    @auth.route('/auth/signup', methods=['POST'])
    def signup():
        errors = validate_user_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        data = request.get_json()
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        otherName = data.get('otherName')
        email = data.get('email')
        phoneNumber = data.get('phoneNumber')
        passportUrl = data.get('passportUrl')
        password = data.get('password')

        if isBlank(firstName):
            return make_response(jsonify({
                "status": 400,
                "message": "firstName cannot be blank",
            }), 400)

        if isBlank(lastName):
            return make_response(jsonify({
                "status": 400,
                "message": "lastName cannot be blank",
            }), 400)

        if isBlank(otherName):
            return make_response(jsonify({
                "status": 400,
                "message": "otherName cannot be blank",
            }), 400)

        if isBlank(email):
            return make_response(jsonify({
                "status": 400,
                "message": "email cannot be blank",
            }), 400)

        if isBlank(phoneNumber):
            return make_response(jsonify({
                "status": 400,
                "message": "phoneNumber cannot be blank",
            }), 400)

        if isBlank(passportUrl):
            return make_response(jsonify({
                "status": 400,
                "message": "passportUrl cannot be blank",
            }), 400)

        if isBlank(password):
            return make_response(jsonify({
                "status": 400,
                "message": "password cannot be blank",
            }), 400)

        if not validEmail(email):
            return make_response(jsonify({
                "status": 400,
                "message": "invalid email address",
            }), 400)

        if not validUrl(passportUrl):
            return make_response(jsonify({
                "status": 400,
                "message": "invalid image url",
            }), 400)

        if not isinstance(firstName, str):
            return make_response(jsonify({
                "status": 400,
                "message": "firstName must be a string",
        }), 400)

        if not isinstance(lastName, str):
            return make_response(jsonify({
                "status": 400,
                "message": "lastName must be a string",
        }), 400)

        if not isinstance(otherName, str):
            return make_response(jsonify({
                "status": 400,
                "message": "otherName must be a string",
        }), 400)

        if User().search(email):
            return make_response(jsonify({
                "status": 400,
                "message": "A user with such email already exists!",
        }), 400)
            
        user = User().create_user(firstName, lastName, otherName, email,
                                  phoneNumber, passportUrl, password)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": user
        }), 201)


class Login:
    @auth.route('/auth/login', methods=['POST'])
    def login():
        errors = validate_login_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not validEmail(email):
            return make_response(jsonify({
                "status": 400,
                "message": "invalid email address",
            }), 400)

        if isBlank(password):
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
