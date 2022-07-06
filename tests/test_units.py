import random
import pytest
from src.domain.entities.game import Game
from src.domain.entities.property import Property


class TestProperties:

    def test_should_create_property(self):
        property = Property(price=250000.50, rental=500.00,
                            owner="Marcelino Avelar", status='purchased')
        assert property.price == 250000.50
        assert property.rental == 500.00
        assert property.status == 'purchased'
        assert property.owner == "Marcelino Avelar"

    def test_should_create_property_whitout_owner(self):
        property = Property(price=250000.50, rental=500.00)
        assert property.price == 250000.50
        assert property.rental == 500.00
        assert property.status == 'available'
        assert property.owner == None

    def test_should_not_create_invalid_property(self):
        with pytest.raises(ValueError, match='Invalid price'):
            Property(price=0.0, rental=0.1,
                     owner="Marcelino Avelar", status='purchased')
        with pytest.raises(ValueError, match='Invalid rental'):
            Property(price=0.1, rental=0.0,
                     owner="Marcelino Avelar", status='purchased')


class TestGame:

    def test_should_create_game(sefl):
        properties = []
        for i in range(20):
            price = round(random.uniform(100.00, 999.99), 2)
            rental = round(random.uniform(1.00, 59.99), 2)
            properties.append(Property(price=price,rental=rental))
        game = Game(properties)
        assert len(game.properties) == 20

    def test_should_create_game(sefl):
        with pytest.raises(ValueError, match='Invalid number of properties'):
            properties = []
            for i in range(19):
                price = round(random.uniform(100.00, 999.99), 2)
                rental = round(random.uniform(1.00, 59.99), 2)
                properties.append(Property(price=price,rental=rental))
            game = Game(properties)