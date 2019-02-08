from flask import Flask
from instance.config import app_config
from app.api.v1.views.party import party as party
from app.api.v1.views.office import office as office

def create_app(config_name):
    """ This method creates a flask application """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.register_blueprint(party)
    app.register_blueprint(office)

    return app