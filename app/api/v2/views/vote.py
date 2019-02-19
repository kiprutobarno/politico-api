from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.vote import Vote
from utils.validations import *
from functools import wraps
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                jwt_refresh_token_required, get_jwt_identity, verify_jwt_in_request, get_jwt_claims, get_raw_jwt)
from utils.validations import validate_login_key_pair_values

vote = Blueprint('vote', __name__)

class CandidateEndPoint:
    """Candidate API Endpoints"""

    @vote.route('/votes/', methods=["POST"])

    @jwt_required    
    def vote():
        """ Register candidate endpoint """

        data = request.get_json()
        office = data.get('office')
        candidate = data.get('candidate')
        voter = data.get('voter')
        Vote().vote(office, candidate, voter)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": Vote().get(voter)
        }), 201)