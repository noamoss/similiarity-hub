import pytest
from flask_fixtures import FixturesMixin
from similarity.models import Item, Entity


@pytest.mark.skip
class TestDBCAlls(FixturesMixin):
    fixtures = ['./fixtures/entity.json', './fixtures/item.json']

    def test_number_of_entites(app):
        entities = Entity.query.all()
        assert len(entities) == Entity.query.count() == 3

    def test_number_of_items(app):
        with app:
            items = Item.query.all()
            assert len(items) == Item.query.count() == 1
