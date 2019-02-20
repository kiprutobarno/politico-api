from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.user import User
from utils.validations import error, validEmail, validUrl, validate_login_key_pair_values,\
    isBlank, validate_user_key_pair_values, check_for_blanks, success, validPassword
from utils.helpers import jwt_required, create_access_token

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

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if not validEmail(email):
            return error(400, "invalid email address")

        if not validUrl(passportUrl):
            return error(400, "invalid image url")

        if not isinstance(firstName, str):
            return error(400, "firstName must be a string")

        if not isinstance(lastName, str):
            return error(400, "lastName must be a string")

        if not isinstance(otherName, str):
            return error(400, "otherName must be a string")

        if User().search(email):
            return error(400, "A user with such email already exists!")

        if not validPassword(password):
            return error(400, "Weak password!")

        return success(201, "Success", User().create_user(firstName, lastName, otherName, email,
                                                          phoneNumber, passportUrl, password)), 201


class Login:
    @jwt_required
    @auth.route('/auth/login', methods=['POST'])
    def login():
        errors = validate_login_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if not validEmail(email):
            return error(400, "invalid email address")
        if not User().search(email):
            return error(403, "That email is not registered")

        user = User().login(email, password)

        if user:
            access_token = create_access_token(identity=user[7])
            return success(201, "Success", [{
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
            }]), 201
        return error(401, "wrong login credentials"), 401
