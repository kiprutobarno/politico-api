from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.office import Office
from utils.validations import *
from functools import wraps
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                jwt_refresh_token_required, get_jwt_identity, verify_jwt_in_request, get_jwt_claims, get_raw_jwt)
from utils.validations import validate_login_key_pair_values

office_version_2 = Blueprint('office_version_2', __name__)

class OfficeEndPoint:
    """Party API Endpoints"""

    @office_version_2.route('/offices', methods=["POST"])

    @jwt_required    
    def office():
        """ Create office endpoint """

        data = request.get_json()
        name = data.get('name')
        officeType = data.get('officeType')

        if name == "":
            return make_response(jsonify({
                "status": 400,
                "message": "name cannot be blank",
            }), 400)

        if officeType == "":
            return make_response(jsonify({
                "status": 400,
                "message": "type cannot be blank",
            }), 400)

        if not isinstance(name, str):
            return make_response(jsonify({
                "status": 400,
                "message": "name must be a string",
            }), 400)

        if not isinstance(officeType, str):
            return make_response(jsonify({
                "status": 400,
                "message": "type must be a string",
            }), 400)

        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": Office().create_office(name, officeType)
        }), 201)

    @office_version_2.route('/offices', methods=["GET"])
    @jwt_required
    def get_offices():
        """ Get all offices endpoint """
    
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Office().get_all_offices()
        }), 200)

    @office_version_2.route('/offices/<int:id>', methods=["GET"])
    @jwt_required
    def get_specific_party(id):
        """ Get a specific political office """
        
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Office().get_specific_office(id)
        }), 200)