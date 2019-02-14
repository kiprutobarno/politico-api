from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.user import User
from utils.validations import *

auth = Blueprint('auth', __name__, url_prefix='/api/v2/auth')

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