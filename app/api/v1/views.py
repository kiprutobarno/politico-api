from flask import Blueprint, make_response, request, jsonify
from .models import Party

api = Blueprint('api', __name__, url_prefix='/api/v1')


class PartiesEndPoint:
    """Party API Endpoints"""

    @api.route('/parties', methods=["POST"])
    def post():
        """ Create party endpoint """
        data = request.get_json()
        name = data['name']
        headquarters = data['hqAddress']
        logoUrl = data['logoUrl']

        party = Party().create_party(name, headquarters, logoUrl)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": party
        }), 201)

    @api.route('/parties', methods=["GET"])
    def get():
        """ Get all parties endpoint """
        parties = Party().get_all_parties()
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": parties
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

    @api.route('/parties/<int:id>', methods=['PATCH'])
    def patch(id):
        """ Update specific political party """
        data = request.get_json()

        party = Party().edit_party(id, data)
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": party
        }), 200)

    @api.route('/parties/<int:id>', methods=["DELETE"])
    def delete(id):
        """ Delete specific political party """
        party = Party().delete_party(id)
        return make_response(jsonify({
            "status": 200,
            "message": "Success"
        }), 200)