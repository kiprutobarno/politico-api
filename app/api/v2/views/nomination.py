from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.nomination import Nomination
from utils.validations import validate_party_key_pair_values, \
    error, validUrl, check_for_blanks, check_for_non_ints, success
from utils.helpers import admin_required
from utils.validations import validate_login_key_pair_values

nomination = Blueprint('nomination', __name__)


class selfNomination:
    """Express interest endpoint"""

    @nomination.route('/self_nomination', methods=['POST'])
    def self_nomination():
        """Self nominations endpoint"""

        data = request.get_json()

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if check_for_non_ints(data):
            return error(400, "{} must be an integer".format(', '.join(check_for_non_ints(data))))

        user = data.get('user')
        party = data.get('party')
        office = data.get('office')
        if Nomination().alreadyExpressed(user):
            return error(400, "You have already expressed interest in an office!")

        return success(201, "Candidate registration successfull!", Nomination().expressInterest(user, party, office)), 201
