import random
import pytest
from src.domain.entities.player import (
    Player, PlayerInpulsive, PlayerPicky, PlayerCautious, PlayerRandom
)
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
            properties.append(Property(price=price, rental=rental))
        game = Game(properties)
        assert len(game.properties) == 20

    def test_should_create_game(sefl):
        with pytest.raises(ValueError, match='Invalid number of properties'):
            properties = []
            for i in range(19):
                price = round(random.uniform(100.00, 999.99), 2)
                rental = round(random.uniform(1.00, 59.99), 2)
                properties.append(Property(price=price, rental=rental))
            game = Game(properties)


class TestPlayer:

    def test_should_create_player(sefl):
        player = Player(balance=1500)
        assert player.balance == 1500

    def test_should_not_player_with_invalid_banalce(self):
        with pytest.raises(ValueError, match='Invalid balance'):
            Player(balance=0.0)

    def test_should_create_player_impulsive(self):
        player = PlayerInpulsive(balance=1500)
        assert player.profile == "impulsive"

    def test_should_purchase_property_inpulsive_player(self):
        property_free = Property(price=150.00, rental=1.50)
        player = PlayerInpulsive(balance=500)
        assert player.evaluate_purchase(property_free) == True

        property_with_owner = Property(price=150.00, rental=1.50,
                                       owner="Marcelino Avelar", status='purchased')
        player = PlayerInpulsive(balance=500)
        assert player.evaluate_purchase(property_with_owner) == True

        property_with_with_price_larger_banlance = Property(price=600.00, rental=1.50,
                                                            owner="Marcelino Avelar", status='purchased')
        player = PlayerInpulsive(balance=500)
        assert player.evaluate_purchase(
            property_with_with_price_larger_banlance) == True

    def test_should_purchase_property_picky_player(self):
        player = PlayerPicky(balance=1500)
        assert player.profile == "picky"

    def test_should_purchase_property_picky_player(self):
        property_free = Property(price=150.00, rental=50.50)
        player = PlayerPicky(balance=500)
        assert player.evaluate_purchase(property_free) == True

        property_with_owner = Property(price=150.00, rental=50.50,
                                       owner="Marcelino Avelar", status='purchased')
        player = PlayerPicky(balance=500)
        assert player.evaluate_purchase(property_with_owner) == True

        property_with_with_price_larger_banlance = Property(price=600.00, rental=50.50,
                                                            owner="Marcelino Avelar", status='purchased')
        player = PlayerPicky(balance=500)
        assert player.evaluate_purchase(
            property_with_with_price_larger_banlance) == True

    def test_should_not_purchase_property_picky_player_with_rental_large(self):
        property = Property(price=150.00, rental=49.99)
        player = PlayerPicky(balance=500)
        assert player.evaluate_purchase(property) == False

    def test_should_purchase_property_cautious_player(self):
        player = PlayerCautious(balance=1500)
        assert player.profile == "cautious"

    def test_should_purchase_property_cautious_player(self):
        property_free = Property(price=150.00, rental=50.50)
        player = PlayerCautious(balance=500)
        assert player.evaluate_purchase(property_free) == True

        property_with_owner = Property(price=150.00, rental=50.50,
                                       owner="Marcelino Avelar", status='purchased')
        player = PlayerCautious(balance=500)
        assert player.evaluate_purchase(property_with_owner) == True

        property_with_with_price_larger_banlance = Property(price=520.00, rental=50.50,
                                                            owner="Marcelino Avelar", status='purchased')
        player = PlayerCautious(balance=600)
        assert player.evaluate_purchase(
            property_with_with_price_larger_banlance) == True

    def test_should_not_purchase_property_cautious_player_with_price_large(self):
        property = Property(price=150.00, rental=50.50)
        player = PlayerCautious(balance=90.0)
        assert player.evaluate_purchase(property) == False

    def test_should_purchase_property_cautious_player(self):
        player = PlayerRandom(balance=1500)
        assert player.profile == "random"

    def test_should_purchase_property_random(self):
        property = Property(price=150.00, rental=50.50)
        player = PlayerRandom(balance=90.0)
        assert isinstance(player.evaluate_purchase(property), bool)