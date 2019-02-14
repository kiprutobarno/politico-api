import os

postgres_link="postgres://admin:admin123@localhost:5432/"
database_name='politico'

class Config:
    """ Parent configuration class """
    DEBUG = False
    APP_SETTINGS = os.getenv('development')
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_BLACKLIST_ENABLED = os.getenv('JWT_BLACKLIST_ENABLED')
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]

class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True
    TESTING = False
    DATABASE_URI = postgres_link + database_name
    os.environ['ENV'] = 'development'


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database"""
    TESTING = True
    DEBUG = True
    DATABASE_URI = postgres_link + database_name + '_test'
    os.environ['ENV'] = 'testing'


app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig
}