import pytest
from similarity import create_app, db


@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('config.TestingConfig')
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
