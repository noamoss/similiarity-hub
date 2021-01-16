class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ""

    SESSION_COOKIE_SECURE = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    DB_HOST = ""
    DB_NAME = ""
    DB_PORT = ""
    DB_USERNAME = ""
    DB_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ""

    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    pass