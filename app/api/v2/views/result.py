from flask import Blueprint, make_response, request, jsonify
from app.api.v2.models.result import Result
from utils.validations import success, error, response
from utils.helpers import jwt_required

result = Blueprint('result', __name__)


class ResultEndPoint:
    """Results API Endpoints"""

    @result.route('/office/<int:id>/result', methods=["GET"])
    @jwt_required
    def get(id):
        """ Register candidate endpoint """
        if not Result().search(id):
            return error(400, "Such an office was not available in this election cycle!")

        if Result().search(id) and len(Result().get(id)) <= 0:
            return response(200, "Kindly be patient, results will be availed shortly!")
        return success(200, "Election Results", Result().get(id))

