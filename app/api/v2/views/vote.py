from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.vote import Vote
from functools import wraps
from utils.validations import validate_office_key_pair_values, error, check_for_blanks, check_for_non_ints, success
from utils.helpers import jwt_required

vote = Blueprint('vote', __name__)


class VoteEndPoint:
    """Vote API Endpoint"""

    @vote.route('/votes/', methods=["POST"])
    @jwt_required
    def vote():
        """ Vote endpoint """

        data = request.get_json()
        if check_for_blanks(data):
            return error(400, "{} cannot be blank".format(', '.join(check_for_blanks(data))))

        if check_for_non_ints(data):
            return error(400, "{} must be an integer".format(', '.join(check_for_non_ints(data))))
        office = data.get('office')
        candidate = data.get('candidate')
        voter = data.get('voter')

        if not Vote().search_office(office):
            return error(400, "Sorry, such elective office is not available!")

        if not Vote().search_candidate(candidate):
            return error(400, "Sorry, such a candidate is not registered!")

        if Vote().search(office, voter):
            return error(400, "Sorry, you have already voted!")
        Vote().vote(office, candidate, voter)
        return success(201, "Thanks for voting, your vote will count!", Vote().get(voter)), 201
