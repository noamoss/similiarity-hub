import pytest

from similarity import create_app, db
from similarity.config import TestingConfig


@pytest.fixture
def app():
    def _app(config_class):
        app = create_app(config_class)
        app.test_request_context().push()

        if config_class is TestingConfig:
            # Always starting with an empty DB.
            db.drop_all()
            db.create_all()

        return app

    yield _app
    db.session.remove()
    if str(db.engine.url) == TestingConfig.SQLALCHEMY_DATABASE_URI:
        db.drop_all()


@pytest.fixture
def client():
    app = create_app(TestingConfig)
    yield app.test_client()
