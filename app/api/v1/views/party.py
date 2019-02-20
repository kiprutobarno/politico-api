from flask import Blueprint, make_response, request, jsonify
from app.api.v1.models.party import Party
from utils.validations import isBlank,  validate_party_key_pair_values, \
    error, validUrl, check_for_blanks, check_for_non_strings, success

party = Blueprint('party', __name__)


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

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if not validUrl(logoUrl):
            return error(400, "Invalid logo url")

        if check_for_non_strings(data):
            return error(400, "{} must be a string".format(', '.join(check_for_non_strings(data))))

        if Party().search(name):
            return error(400, "Such a party is already registered!")

        return success(201, "Success", Party().create_party(name, hqAddress, logoUrl))

    @party.route('/parties', methods=["GET"])
    def get_parties():
        """ Get all parties endpoint """
        if not Party().parties:
            return error(404, "No party is currently registered")

        return success(200, "Success", Party().get_all_parties())

    @party.route('/parties/<int:id>', methods=["GET"])
    def get_specific_party(id):
        """ Get a specific political party """

        if not Party().parties or len(Party().parties) < id:
            return error(404, "Sorry, no such party exists")

        return success(200, "Success", Party().get_specific_party(id))

    @party.route('/parties/<int:id>/<string:name>', methods=['PATCH'])
    def patch_party(id, name):
        """ Edit specific political party """

        errors = validate_party_key_pair_values(request)
        if errors:
            return error(400, "{} key missing".format(', '.join(errors)))

        if not Party().parties or len(Party().parties) < id:
            return error(404, "You cannot edit a non-existent party")

        data = request.get_json()
        name = data.get('name')
        hqAddress = data.get('hqAddress')
        logoUrl = data.get('logoUrl')

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if not validUrl(logoUrl):
            return error(400, "Invalid logo url")

        if check_for_non_strings(data):
            return error(400, "{} must be a string".format(', '.join(check_for_non_strings(data))))

        return success(201, "Success", Party().get_specific_party(id))

    @party.route('/parties/<int:id>', methods=["DELETE"])
    def delete_party(id):
        """ Delete specific political party """
        if id <= 0:
            return error(400, "Unacceptable id format")


        if not Party().get_specific_party(id):
            return error(404, "You cannot delete a non-existent party")
        return success(200, "Success", Party().delete_party(id))
