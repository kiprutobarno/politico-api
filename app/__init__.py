from flask import Flask, make_response, jsonify
from instance.config import app_config
from app.api.v1.views.party import party as party
from app.api.v1.views.office import office as office

def handle_bad_request(e):
    return make_response(
        jsonify(
            {
                "error": "Sorry, request was not understood!",
                "status": 400
            }
        )
    )

def create_app(config_name):
    """ This method creates a flask application """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.register_blueprint(party)
    app.register_blueprint(office)
    app.register_error_handler(400, handle_bad_request)

    return app