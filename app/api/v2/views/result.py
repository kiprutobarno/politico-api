from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.result import Result
from utils.validations import *
from functools import wraps
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required,
                                jwt_refresh_token_required, get_jwt_identity, verify_jwt_in_request, get_jwt_claims, get_raw_jwt)
from utils.validations import validate_login_key_pair_values

result = Blueprint('result', __name__)

class ResultEndPoint:
    """Results API Endpoints"""

    @result.route('/office/<int:id>/result', methods=["GET"])

    @jwt_required    
    def get(id):
        """ Register candidate endpoint """
        print(Result().get(id))
        return make_response(jsonify({
            "status": 200,
            "message": "Success",
            "data": Result().get(id)
        }), 200)