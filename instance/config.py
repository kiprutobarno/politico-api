import os


class Config:
    """ Parent configuration class """
    DEBUG = False


class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database"""
    TESTING = True
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}