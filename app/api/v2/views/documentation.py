from flask import redirect, Blueprint

documentation = Blueprint('documentation', __name__)


class Documentation:
    @documentation.route('/', methods=['GET'])
    def home():
        return redirect('https://app.swaggerhub.com/apis-docs/kipruto/politico-api/1.0')
