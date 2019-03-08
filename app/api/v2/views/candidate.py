from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.candidate import Candidate
from utils.validations import validate_party_key_pair_values, \
    error, validUrl, check_for_blanks, check_for_non_ints, success
from utils.helpers import admin_required, jwt_required
from utils.validations import validate_login_key_pair_values

candidate = Blueprint('candidate', __name__)


class CandidateEndPoint:
    """Candidate API Endpoints"""

    @candidate.route('/office/<int:office>/register', methods=["POST"])
    @admin_required
    def register(office):
        """ Register candidate endpoint """

        data = request.get_json()

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if check_for_non_ints(data):
            return error(400, "{} must be an integer".format(', '.join(check_for_non_ints(data))))

        candidate = data.get('candidate')
        office = Candidate().getOffice(candidate)
        party = Candidate().getParty(candidate)

        if Candidate().checkApproved(candidate):
            return error(400, "This aspirant is already approved!")

        if Candidate().party_has_candidate(candidate):
            return error(400, "This party has an already approved candidate!")

        Candidate().approve(candidate)
        return success(201, "Candidate registration successfull!", Candidate().get(candidate)), 201

    @candidate.route('/office/<int:office>/deregister', methods=["POST"])
    @admin_required
    def deregister(office):
        """ Deregister candidate endpoint """

        data = request.get_json()

        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if check_for_non_ints(data):
            return error(400, "{} must be an integer".format(', '.join(check_for_non_ints(data))))

        candidate = data.get('candidate')
        office = Candidate().getOffice(candidate)
        party = Candidate().getParty(candidate)

        if not Candidate().checkApproved(candidate):
            return error(400, "This politician had not been approved!")
        Candidate().unApprove(candidate)
        return success(201, "This candidates registration has been revoked!", Candidate().get(candidate)), 201

    @candidate.route('/office/<int:office>/politicians', methods=["GET"])
    @admin_required
    def get_politicians(office):
        """ Get specific office candidates endpoint """
        return success(200, "Success", Candidate().get_all_politicians())

    @candidate.route('/candidates', methods=["GET"])
    @jwt_required
    def get_candidates():
        """ Get all approved candidates endpoint """
        return success(200, "Success", Candidate().get_all_candidates())

    @candidate.route('office/<int:id>/candidates', methods=["GET"])
    @jwt_required
    def get_office_candidates(id):
        """ Get all approved candidates endpoint """
        return success(200, "Success", Candidate().get_candidates_per_office(id))
