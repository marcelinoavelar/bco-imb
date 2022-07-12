import random
from src.applications.services.purchase_property_service import PurchasePropertyService
from src.domain.entities.property import Property
from src.domain.entities.player import Player


class GameRound:

    def __init__(self, properties: list[Property], players: list[Player]) -> None:
        self.properties = properties
        self.players = players

    def execute(self, rounds: int) -> bool:

        player_positons = dict({})
        for player in self.players:
            player_positons[player.name] = 0

        for i in range(rounds):
            for player in self.players:
                plus_balance = False
                progess = round(random.uniform(1, 6))
                player_positons[player.name] += progess
                if player_positons[player.name]+progess >= len(self.properties):
                    progess = progess-len(self.properties)
                    plus_balance = True
                property = self.properties[progess-1:progess][0]
                purchase_property_service = PurchasePropertyService()
                output = purchase_property_service.purchase(property, player)
                if not output:
                    if property.owner != None:
                        player.pay_rental(property)
                if player.balance < 0:
                    property.free()
                    self.players.remove(player)
                else:
                    if plus_balance:
                        player.add_balance(100)

            if len(self.players) == 1:
                break


        print(f'\n Winer -> {self.players} \n')
