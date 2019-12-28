import os
basedir = os.path.abspath(os.path.dirname(__file__))

#source env/bin/activate
#export APP_SETTINGS="main_config.DevelopmentConfig"

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '#Main Flask 567!'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
