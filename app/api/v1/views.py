from flask import Blueprint, make_response, request, jsonify
from .models import Party, Office, parties, offices
from .validations import *

api = Blueprint('api', __name__, url_prefix='/api/v1')


class PartiesEndPoint:
    """Party API Endpoints"""

    @api.route('/parties', methods=["POST"])
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

        party = Party().create_party(name, hqAddress, logoUrl)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": party
        }), 201)

    @api.route('/parties', methods=["GET"])
    def get_parties():
        """ Get all parties endpoint """
        if len(parties) < 1:
            return make_response(jsonify({
                "status": 404,
                "message": "No party is currently registered",
        }), 404)
    
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Party().get_all_parties()
        }), 200)

    @api.route('/parties/<int:id>', methods=["GET"])
    def get_specific_party(id):
        """ Get a specific political party """
        party = Party().get_specific_party(id)
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": party
        }), 200)

    @api.route('/parties/<int:id>/<string:name>', methods=['PATCH'])
    def patch_party(id, name):
        """ Update specific political party """
        data = request.get_json()

        party = Party().edit_party(id, name, data)
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": party
        }), 200)

    @api.route('/parties/<int:id>', methods=["DELETE"])
    def delete_party(id):
        """ Delete specific political party """
        party = Party().delete_party(id)
        return make_response(jsonify({
            "status": 200,
            "message": "Success"
        }), 200)


class OfficesEndpoint:
    """Office API Endpoints"""

    @api.route('/offices', methods=['POST'])
    def post_office():
        """ Create office endpoint """
        
        errors = validate_office_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))


        data = request.get_json()
        office_type=data.get('type')
        name=data.get('name')

        if name == "":
            return make_response(jsonify({
                "status": 400,
                "message": "name cannot be blank",
        }), 400)

        if office_type == "":
            return make_response(jsonify({
                "status": 400,
                "message": "type cannot be blank",
        }), 400)

        if type(name) != str:
            return make_response(jsonify({
                "status": 400,
                "message": "name must be a string",
        }), 400)

        if type(office_type) != str:
            return make_response(jsonify({
                "status": 400,
                "message": "type must be a string",
        }), 400)

        
        office = Office().create_office(office_type, name)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": office
        }), 201)

    @api.route('/offices', methods=["GET"])
    def get_offices():
        """ Get all offices endpoint """

        if len(offices) < 1:
            return make_response(jsonify({
                "status": 404,
                "message": "Sorry, no government office is currently available, try again later",
        }), 404)

        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Office().get_all_offices()
        }), 200)

    @api.route('/offices/<int:id>', methods=["GET"])
    def get_specific_office(id):
        """ Get a specific political office """

        if len(offices) < 1:
            return make_response(jsonify({
                "status": 404,
                "message": "Sorry, no such office exists, try again later!",
        }), 404)

        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Office().get_specific_office(id)
        }), 200)
