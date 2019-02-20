from flask import Flask, make_response
from flask_jwt_extended import JWTManager
from instance.config import app_config
from app.api.v1.views.party import party as party
from app.api.v1.views.office import office as office
from app.api.v2.views.user import auth as auth
from app.api.v2.views.party import party_version_2 as party_version_2
from app.api.v2.views.office import office_version_2 as office_version_2
from app.api.v2.views.candidate import candidate as candidate
from app.api.v2.views.vote import vote as vote
from app.api.v2.views.result import result as result
from app.api.v2.db import create_tables, default_admin
from app.api.v2.models.blacklist import Blacklist
from utils.validations import error


def handle_bad_request(e):
    return error(400, "Sorry, request was not understood!")


def handle_method_not_allowed(e):
    return error(405, "Sorry, request method not allowed!")


def handle_not_found(e):
    return error(404, "The information you are looking for cannot be found!")


def create_app(config_name):
    """ This method creates a flask application """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.app_context().push()
    create_tables()
    default_admin()
    # app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = "sweet_secret"
    app.config['JWT_SECRET_KEY'] = "jwt_sweet_secret"
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    # app.config['APP_SETTINGS'] = "development"
    app.register_blueprint(party, url_prefix='/api/v1')
    app.register_blueprint(office, url_prefix='/api/v1')
    app.register_blueprint(auth, url_prefix='/api/v2')
    app.register_blueprint(party_version_2, url_prefix='/api/v2')
    app.register_blueprint(office_version_2, url_prefix='/api/v2')
    app.register_blueprint(candidate, url_prefix='/api/v2')
    app.register_blueprint(vote, url_prefix='/api/v2')
    app.register_blueprint(result, url_prefix='/api/v2')

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
