from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.candidate import Candidate
from utils.validations import *
from functools import wraps
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                jwt_refresh_token_required, get_jwt_identity, verify_jwt_in_request, get_jwt_claims, get_raw_jwt)
from utils.validations import validate_login_key_pair_values

candidate = Blueprint('candidate', __name__)

class CandidateEndPoint:
    """Candidate API Endpoints"""

    @candidate.route('/office/<int:office>/register', methods=["POST"])

    @jwt_required    
    def register(office):
        """ Register candidate endpoint """

        data = request.get_json()
        office = data.get('office')
        party = data.get('party')
        candidate = data.get('candidate')

        if isBlank(office):
            return make_response(jsonify({
                "status": 400,
                "message": "office cannot be blank",
            }), 400)

        if isBlank(party):
            return make_response(jsonify({
                "status": 400,
                "message": "party cannot be blank",
            }), 400)

        if isBlank(candidate):
            return make_response(jsonify({
                "status": 400,
                "message": "candidate cannot be blank",
            }), 400)

        if not isinstance(office, int):
            return make_response(jsonify({
                "status": 400,
                "message": "officeId must be an integer",
        }), 400)

        if not isinstance(party, int):
            return make_response(jsonify({
                "status": 400,
                "message": "partyId must be an integer",
        }), 400)

        if not isinstance(candidate, int):
            return make_response(jsonify({
                "status": 400,
                "message": "candidateId must be an integer",
        }), 400)

        if Candidate().search(candidate):
            return make_response(jsonify({
                "status": 400,
                "message": "Candidate is already registered!",
        }), 400)


        Candidate().register(office, party, candidate)
        Candidate().update(candidate)
        return make_response(jsonify({
            "status": 201,
            "message": "Success",
            "data": Candidate().get(office)
        }), 201)