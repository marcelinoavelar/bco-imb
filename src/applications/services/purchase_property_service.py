from src.domain.entities.property import Property
from src.domain.entities.player import Player


class PurchasePropertyService:

    def purchase(self, property: Property, player: Player) -> bool:

        if not property.status == 'available':
            return False

        if property.price > player.balance:
            return False

        if not player.evaluate_purchase(property):
            return False
        property.purchase(player.name)
        player.purchase(property.price)
        return True
