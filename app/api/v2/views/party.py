from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.party import Party
from utils.validations import isBlank,  validate_party_key_pair_values, \
    error, validUrl, check_for_blanks, check_for_non_strings, success, response
from utils.helpers import admin_required, jwt_required


party_version_2 = Blueprint('party_version_2', __name__)


class PartyEndPoint:
    """Party API Endpoints"""

    @party_version_2.route('/parties', methods=["POST"])
    @admin_required
    def party():
        """ Create party endpoint """
        errors = validate_party_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        data = request.get_json()
        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        name = data.get('name')
        hqAddress = data.get('hqAddress')
        logoUrl = data.get('logoUrl')

        if check_for_non_strings(data):
            return error(400, "{} must be a string".format(', '.join(check_for_non_strings(data))))

        if not validUrl(logoUrl):
            return error(400, "Invalid logo url")

        if Party().search(name):
            return error(400, "Such a party is already registered!")
        return success(201, "Success", Party().create_party(name, hqAddress, logoUrl)), 201

    @party_version_2.route('/parties', methods=["GET"])
    @jwt_required
    def get_parties():
        """ Get all parties endpoint """

        if not Party().get_all_parties():
            return error(404, "No party is currently registered")

        return success(200, "Success", Party().get_all_parties())

    @party_version_2.route('/parties/<int:id>', methods=["GET"])
    @jwt_required
    def get_specific_party(id):
        """ Get a specific political party """
        if id <= 0:
            return error(400, "Unacceptable id format")
        if not Party().get_specific_party(id):
            return error(404, "Sorry, no such party exists")
        return success(200, "Success", Party().get_specific_party(id))

    @party_version_2.route(
        '/parties/<int:id>/<string:name>',
        methods=['PATCH'])
    @admin_required
    def patch_party(id, name):
        """ Edit specific political party """
        if id <= 0:
            return error(400, "Unacceptable id format")

        errors = validate_party_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        data = request.get_json()

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        name = data.get('name')
        hqAddress = data.get('hqAddress')
        logoUrl = data.get('logoUrl')

        if not validUrl(logoUrl):
            return error(400, "Invalid logo url")

        if check_for_non_strings(data):
            return error(400, "{} must be a string".format(', '.join(check_for_non_strings(data))))

        Party().edit_party(id, name, data)
        return success(201, "Party details successfully updated!", Party().get_specific_party(id)), 201

    @party_version_2.route('/parties/<int:id>', methods=["DELETE"])
    @admin_required
    def delete_party(id):
        """ Delete specific political party """
        if id <= 0:
            return error(400, "Unacceptable id format")

        if not Party().get_specific_party(id):
            return error(404, "You cannot delete a non-existent party")

        Party().delete_party(id)
        return response(200, "Party successfully deleted!")
