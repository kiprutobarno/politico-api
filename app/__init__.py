from flask import Flask
from instance.config import app_config
from app.api.v1.views.views import api as v1

def create_app(config_name):
    """ Create flask application method """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.register_blueprint(v1)

    return app