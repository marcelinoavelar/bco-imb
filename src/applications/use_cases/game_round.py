import random
from src.applications.services.purchase_property_service import PurchasePropertyService
from src.domain.entities.property import Property
from src.domain.entities.player import Player


class GameRound:

    def __init__(self, properties: list[Property], players: list[Player]) -> dict:
        self.properties = properties
        self.players = players
        self.players_positons = self.init_positions()

    def execute(self, rounds: int) -> bool:

        for i in range(rounds):
            for player in self.players:
                if len(self.players) == 1:
                    output = {
                        "rounds": i,
                        "players": len(self.players),
                        "winner": self.players[0].__class__.__name__,
                        "timeout": False
                    }
                    return output
                progress, plus_balance = self.get_progress(player)
                property = self.properties[progress-1:progress][0]
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

            if i+1 == rounds:
                winner = self.game_leader()
                output = {
                    "rounds": i+1,
                    "players": len(self.players),
                    "winner": winner.__class__.__name__,
                    "timeout": True
                }
                return output

    def init_positions(self) -> None:
        players_positons = dict({})
        for player in self.players:
            players_positons[player.name] = 0
        return players_positons

    def get_progress(self, player: Player) -> tuple[int, bool]:
        plus_balance = False
        progress = round(random.uniform(1, 6))
        self.players_positons[player.name] += progress
        if self.players_positons[player.name]+progress >= len(self.properties):
            progress = progress-len(self.properties)
            plus_balance = True
        return progress, plus_balance

    def game_leader(self) -> Player:
        winner = self.players[0]
        for player in self.players[1:len(self.players)]:
            if player.balance > winner.balance:
                winner = player
        return winner
