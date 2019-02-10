from flask import Blueprint, make_response, request, jsonify
from app.api.v1.models.party import Party, parties
from utils.validations import *

party = Blueprint('party', __name__, url_prefix='/api/v1')

class PartiesEndPoint:
    """Party API Endpoints"""

    @party.route('/parties', methods=["POST"])
    def post_party():
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

        if any(party['name'] == name for party in parties):
            return make_response(jsonify({
                "status": 400,
                "message": "That party already exists!",
        }), 400)

        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": Party().create_party(name, hqAddress, logoUrl)
        }), 201)

    @party.route('/parties', methods=["GET"])
    def get_parties():
        """ Get all parties endpoint """
        if not Party().parties:
            return make_response(jsonify({
                "status": 404,
                "message": "No party is currently registered",
        }), 404)
    
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Party().get_all_parties()
        }), 200)

    @party.route('/parties/<int:id>', methods=["GET"])
    def get_specific_party(id):
        """ Get a specific political party """
        
        if not Party().parties or len(Party().parties) < id:
            return make_response(jsonify({
                "status": 404,
                "message": "Sorry, no such party exists",
        }), 404)
        
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Party().get_specific_party(id)
        }), 200)

    @party.route('/parties/<int:id>/<string:name>', methods=['PATCH'])
    def patch_party(id, name):
        """ Edit specific political party """

        errors = validate_party_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        if not Party().parties or len(Party().parties) < id:
            return make_response(jsonify({
                "status": 404,
                "message": "You cannot edit a non-existent party",
        }), 404)
            
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

        
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Party().edit_party(id, name, data)
        }), 200)

    @party.route('/parties/<int:id>', methods=["DELETE"])
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
            
        if not Party().parties:
            return make_response(
                jsonify(
                    {
                        "status": 404,
                        "message": "You cannot delete a non-existent party",
                    }
                ), 404
            )

        party = Party().delete_party(id)
        return make_response(jsonify({
            "status": 200,
            "message": "Success"
        }), 200)