from flask import Flask
from instance.config import app_config
from app.api.v1.views import api as v1

def create_app(config_name):
    """
        This function wraps the creation of a new Flask object
        and returns it after it's loaded up with configuration settings
        using 'app.config'
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    app.register_blueprint(v1, url_prefix='/api/v1/')

    return app