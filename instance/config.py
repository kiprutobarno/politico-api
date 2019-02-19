import os


class Config:
    """ Parent configuration class """
    DEBUG = False
    
class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True
    TESTING = False
    DATABASE_URL =os.getenv('DATABASE')


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database"""
    TESTING = True
    DEBUG = True
    DATABASE_URL =os.getenv('TEST_DATABASE')

app_config = {
    'testing': TestingConfig,
    'development': DevelopmentConfig
}