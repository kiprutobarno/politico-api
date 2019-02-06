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