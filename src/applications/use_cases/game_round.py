from src.applications.services.purchase_property_service import PurchasePropertyService
from src.domain.entities.property import Property
from src.domain.entities.player import Player


class GameRound:

    def execute(self, property: Property, player: Player) -> bool:

        purchase_property_service = PurchasePropertyService()
        output = purchase_property_service.purchase(property, player)
        return output
