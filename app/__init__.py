from flask import Flask, make_response, jsonify
from flask_jwt_extended import JWTManager
from functools import wraps
from instance.config import app_config
from app.api.v1.views.party import party as party
from app.api.v1.views.office import office as office
from app.api.v2.views.user import auth as auth
from app.api.v2.db import create_tables
from app.api.v2.models.blacklist import Blacklist


def handle_bad_request(e):
    return make_response(
        jsonify(
            {
                "error": "Sorry, request was not understood!",
                "status": 400
            }
        )
    )


def handle_method_not_allowed(e):
    return make_response(
        jsonify(
            {
                "error": "Sorry, request method not allowed",
                "status": 405
            }
        )
    )


def handle_not_found(e):
    return make_response(
        jsonify(
            {
                "error": "The information you are looking for cannot be found",
                "status": 404
            }
        )
    )

def create_app(config_name):
    """ This method creates a flask application """
    app = Flask(__name__, instance_relative_config=True)
    create_tables()
    app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = "sweet_secret"
    app.config['JWT_SECRET_KEY'] = "jwt_sweet_secret"
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.config['APP_SETTINGS'] = "development"

    app.register_blueprint(party)
    app.register_blueprint(office)
    app.register_blueprint(auth)
    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(405, handle_method_not_allowed)
    app.register_error_handler(404, handle_not_found)
    jwt = JWTManager(app)

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        return {
            'isAdmin': identity
        }

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        if Blacklist().search(jti):
            return jti

    return app
