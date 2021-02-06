from flask_fixtures import FixturesMixin
from similarity.models import Item, Entity
import os

def test_development_config(app):
    app.config.from_object('config.DevelopmentConfig')
    assert app.config['DEBUG']
    assert not app.config['TESTING']

def test_testing_config(app):
    app.config.from_object('config.TestingConfig')
    assert app.config['DEBUG'] == False
    assert app.config['TESTING']
    assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']

def test_production_config(app):
    app.config.from_object('config.ProductionConfig')
    assert not app.config['DEBUG']
    assert not app.config['TESTING']


class TestDBCAlls(FixturesMixin):
    fixtures = ['entity.json', 'item.json']

    def test_number_of_entites(app):
        entities = Entity.query.all()
        assert len(entities) == Entity.query.count() == 3

    def test_number_of_items(app):
        with app:
            items = Item.query.all()
            assert len(items) == Item.query.count() == 1

