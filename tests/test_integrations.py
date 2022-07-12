from src.applications.services.purchase_property_service import PurchasePropertyService
from src.domain.entities.property import Property
from src.domain.entities.player import *


class TestPurchasePropertyService:

    def test_should_player_inpulsive_purchase_property(self):
        property = Property(price=500.00, rental=5.00)
        player = PlayerInpulsive("Player", balance=1000.00)
        purchase_property_service = PurchasePropertyService()
        output = purchase_property_service.purchase(property, player)
        assert output == True
        assert property.owner == player.name
        assert property.status == "purchased"
        assert player.balance == 500.0

    def test_should_player_picky_purchase_property(self):
        property = Property(price=500.00, rental=50.01)
        player = PlayerPicky("Player", balance=1000.00)
        purchase_property_service = PurchasePropertyService()
        output = purchase_property_service.purchase(property, player)
        assert output == True
        assert property.owner == player.name
        assert property.status == "purchased"
        assert player.balance == 500.0

    def test_should_not_player_picky_purchase_property_low_rental(self):
        property = Property(price=500.00, rental=49.99)
        player = PlayerPicky("Player", balance=1000.00)
        purchase_property_service = PurchasePropertyService()
        output = purchase_property_service.purchase(property, player)
        assert output == False
        assert property.owner == None
        assert property.status == "available"
        assert player.balance == 1000.0

    def test_should_player_cautious_purchase_property(self):
        property = Property(price=500.00, rental=50.01)
        player = PlayerCautious("Player", balance=1000.00)
        purchase_property_service = PurchasePropertyService()
        output = purchase_property_service.purchase(property, player)
        assert output == True
        assert property.owner == player.name
        assert property.status == "purchased"
        assert player.balance == 500.0

    def test_should_not_player_cautious_purchase_property_low_rental(self):
        property = Property(price=500.00, rental=49.99)
        player = PlayerCautious("Player", balance=450.00)
        purchase_property_service = PurchasePropertyService()
        output = purchase_property_service.purchase(property, player)
        assert output == False
        assert property.owner == None
        assert property.status == "available"
        assert player.balance == 450.00
