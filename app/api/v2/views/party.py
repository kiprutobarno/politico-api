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
    def party():
        print(get_jwt_claims()['isAdmin'])
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

        if Party().search(name):
            return make_response(jsonify({
                "status": 400,
                "message": "Such a party is already registered!",
        }), 400)
        
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": Party().create_party(name, hqAddress, logoUrl)
        }), 201)


    @party_version_2.route('/parties', methods=["GET"])

    @admin_required
    def get_parties():
        """ Get all parties endpoint """

        if Party().get_all_parties():
    
            return make_response(
                jsonify(
                    {
                        "status": 200,
                        "message": "Success",
                        "data": Party().get_all_parties()
                    }
                ), 200
            )

        else:
            return make_response(jsonify(
                jsonify(
                        {
                            "status": 200,
                            "message": "Sorry, no party has been currently registered"
                        }
                    ), 200
                )
            )

    @party_version_2.route('/parties/<int:id>', methods=["GET"])
    @jwt_required
    def get_specific_party(id):
        """ Get a specific political party """

        if Party().get_specific_party(id):
        
            return make_response(
                jsonify(
                    {
                        "status": 200,
                        "message": "Success",
                        "data": Party().get_specific_party(id)
                    }
                ), 200
            )

        else:
            return make_response(jsonify(
                jsonify(
                        {
                            "status": 200,
                            "message": "No such party is registered"
                        }
                    ), 200
                )
            )

    @party_version_2.route('/parties/<int:id>', methods=["DELETE"])
    @jwt_required
    def delete_party(id):
        """ Delete specific political party """
        if id <= 0:
            return make_response(
                jsonify(
                    {
                        "status": 400,
                        "message": "Unacceptable id format",
                    }
                ), 400
            )

        party = Party().delete_party(id)
        return make_response(jsonify({
            "status": 200,
            "message": "Party successfull deleted!"
        }), 200)   

    @party_version_2.route('/parties/<int:id>/<string:name>', methods=['PATCH'])
    def patch_party(id, name):
        """ Edit specific political party """

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

        if not isinstance(name, str):
            return make_response(jsonify({
                "status": 400,
                "message": "name must be a string",
        }), 400)

        if not isinstance(hqAddress, str):
            return make_response(jsonify({
                "status": 400,
                "message": "hqAddress must be a string",
        }), 400)

        Party().edit_party(id, name, data)
        
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Party().get_specific_party(id)
        }), 200)             
