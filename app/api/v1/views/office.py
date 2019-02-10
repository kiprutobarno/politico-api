from flask import Blueprint, make_response, request, jsonify
from app.api.v1.models.office import Office, offices
from utils.validations import *

office = Blueprint('office', __name__, url_prefix='/api/v1')

class OfficesEndpoint:
    """Office API Endpoints"""

    @office.route('/offices', methods=['POST'])
    def post_office():
        """ Create office endpoint """

        errors = validate_office_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        data = request.get_json()
        office_type = data.get('type')
        name = data.get('name')

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

        if not isinstance(name, str):
            return make_response(jsonify({
                "status": 400,
                "message": "name must be a string",
            }), 400)

        if not isinstance(office_type, str):
            return make_response(jsonify({
                "status": 400,
                "message": "type must be a string",
            }), 400)

        if any(office['name'] == name for office in offices):
            return make_response(jsonify({
                "status": 400,
                "message": "That office already exists!",
            }), 400)

        office = Office().create_office(office_type, name)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": office
        }), 201)

    @office.route('/offices', methods=["GET"])
    def get_offices():
        """ Get all offices endpoint """
        if not Office().offices:
            return make_response(jsonify({
                "status": 404,
                "message": "Sorry, no government office is currently available, try again later",
            }), 404)
        
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Office().get_all_offices()
        }), 200)

    @office.route('/offices/<int:id>', methods=["GET"])
    def get_specific_office(id):
        """ Get a specific political office """

        if not Office().offices or len(Office().offices) < id:
            return make_response(jsonify({
                "status": 404,
                "message": "Sorry, no such office exists, try again later!",
            }), 404)

        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Office().get_specific_office(id)
        }), 200)
