import os


class Config:
    """ Parent configuration class """
    DEBUG = False


class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True
    TESTING = False
    DATABASE_URI = os.getenv('DATABASE_URI')
    os.environ['ENV'] = 'development'


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database"""
    TESTING = True
    DEBUG = True
    DATABASE_URI = os.getenv('DATABASE_URI')+'_test'
    os.environ['ENV'] = 'testing'


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}