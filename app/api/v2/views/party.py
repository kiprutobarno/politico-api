from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.party import Party
from utils.validations import *
from functools import wraps
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                jwt_refresh_token_required, get_jwt_identity, verify_jwt_in_request, get_jwt_claims, get_raw_jwt)
from utils.validations import validate_login_key_pair_values

party_version_2 = Blueprint('party_version_2', __name__)


class PartyEndPoint:
    """Party API Endpoints"""

    @party_version_2.route('/parties', methods=["POST"])
    @jwt_required
    def party():
        """ Create party endpoint """
        errors = validate_party_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        data = request.get_json()
        name = data.get('name')
        hqAddress = data.get('hqAddress')
        logoUrl = data.get('logoUrl')

        if name == "":
            return make_response(jsonify({
                "status": 400,
                "message": "name cannot be blank",
        }), 400)

        if hqAddress == "":
            return make_response(jsonify({
                "status": 400,
                "message": "hqAddress cannot be blank",
        }), 400)

        if logoUrl == "":
            return make_response(jsonify({
                "status": 400,
                "message": "logoUrl cannot be blank",
        }), 400)

        if type(name) != str:
            return make_response(jsonify({
                "status": 400,
                "message": "name must be a string",
        }), 400)

        if type(hqAddress) != str:
            return make_response(jsonify({
                "status": 400,
                "message": "hqAddress must be a string",
        }), 400)

        # if Party().search(name):
        #     return make_response(jsonify({
        #         "status": 403,
        #         "message": "That party already exists!",
        #     }), 403)

        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": Party().create_party(name, hqAddress, logoUrl)
        }), 201)
