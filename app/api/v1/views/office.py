from flask import Blueprint, make_response, request, jsonify
from app.api.v1.models.office import Office, offices
from utils.validations import validate_office_key_pair_values, error, check_for_blanks, check_for_non_strings, success

office = Blueprint('office', __name__)


class OfficesEndpoint:
    """Office API Endpoints"""

    @office.route('/offices', methods=['POST'])
    def post_office():
        """ Create office endpoint """

        if validate_office_key_pair_values(request):
            return error(400, "{} key missing".format(', '.join(validate_office_key_pair_values(request))))

        data = request.get_json()
       
        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if check_for_non_strings(data):
            return error(400, "{} must be a string".format(', '.join(check_for_non_strings(data))))

        officeType = data.get('officeType')
        name = data.get('name')

        if any(office['name'] == name for office in offices):
            return error(400, "That office already exists!")

        return success(201, "Success", Office().create_office(name, officeType))

    @office.route('/offices', methods=["GET"])
    def get_offices():
        """ Get all offices endpoint """
        if not Office().offices:
            return error(404, "Sorry, no government office is currently available, try again later")

        return success(200, "Success", Office().get_all_offices())

    @office.route('/offices/<int:id>', methods=["GET"])
    def get_specific_office(id):
        """ Get a specific political office """

        if not Office().offices or len(Office().offices) < id:
            return error(404, "Sorry, no such office exists, try again later!")
        return success(200, "Success", Office().get_specific_office(id))
