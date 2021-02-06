class Config(object):
    """
    Set the basic Flask configurations
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''

    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    """
    Set the specific configurations for the Production envrioment
    """
    DB_HOST = ''
    DB_NAME = ''
    DB_PORT = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class DevelopmentConfig(Config):
    """
    Set the specific configurations for the development envrioment
    """
    DEBUG = True
    DB_HOST = ''
    DB_NAME = ''
    DB_PORT = ''
    DB_USERNAME = ''
    DB_PASSWORD = ''
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    """
    Set the specific configurations for the automatic tests
    """
    TESTING = True
