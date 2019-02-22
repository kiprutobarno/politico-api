from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.office import Office
from utils.helpers import admin_required, jwt_required, get_jwt_claims, verify_jwt_in_request
from utils.validations import validate_office_key_pair_values, error, check_for_blanks, \
    check_for_non_strings, success


office_version_2 = Blueprint('office_version_2', __name__)

class OfficeEndPoint:
    """Office API Endpoints"""

    @office_version_2.route('/offices', methods=["POST"])
    @admin_required
    def office():
        """ Create office endpoint """

        if validate_office_key_pair_values(request):
            return error(400, "{} key missing".format(', '.join(validate_office_key_pair_values(request))))

        data = request.get_json()

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if check_for_non_strings(data):
            return error(400, "{} must be a string".format(', '.join(check_for_non_strings(data))))

        name = data.get('name')
        office = data.get('officeType')

        if Office().search(name):
            return error(400, "Such an office is already registered!")

        return success(201, "Office successfully created!", Office().create_office(name, office))


    @office_version_2.route('/offices', methods=["GET"])
    @jwt_required
    def get_offices():
        """ Get all offices endpoint """

        if not Office().get_all_offices():
            return error(404, "Sorry, no government office is currently available, try again later")

        return success(200, "Success", Office().get_all_offices())

    @office_version_2.route('/offices/<int:id>', methods=["GET"])
    @jwt_required
    def get_specific_party(id):
        """ Get a specific political office """
        if id <= 0:
            return error(400, "Unacceptable id format")

        if not Office().get_specific_office(id) or len(Office().get_all_offices()) < id:
            return error(404, "Sorry, no such office exists, try again later!")
        return success(200, "Success", Office().get_specific_office(id))
