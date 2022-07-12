import random
from src.applications.services.purchase_property_service import PurchasePropertyService
from src.domain.entities.property import Property
from src.domain.entities.player import Player


class GameRound:

    def __init__(self, properties: list[Property], players: list[Player]) -> None:
        self.properties = properties
        self.players = players

    def execute(self) -> bool:

        # Init positons
        player_positons = dict({})        
        for player in self.players:
            player_positons[player.name] = 0
        
        for i in range(50):
            print(f'\n $Jogadores atuais ->  {len(self.players)} \n')
            for player in self.players:
                progess = round(random.uniform(1, 6))
                print(f'\n -> {player.name} tem saldo de : {player.balance} \n')
                print(f'\n -> {player.name} jogou o dado : {progess} \n')
                print(f'\n -> {player.name} estava em  : {player_positons[player.name]} \n')
                player_positons[player.name] += progess
                print(f'\n -> {player.name} vai para : {player_positons[player.name]} \n')
                if player_positons[player.name]+progess >= len(self.properties):
                    progess = progess-len(self.properties)
                property = self.properties[progess-1:progess][0]
                print(f'\n -> {player.name} vai tentar comprar propriede de  : R$ {property.price} \n')
                purchase_property_service = PurchasePropertyService()
                output = purchase_property_service.purchase(property, player)
                print(f'\n -> jogador {player.name} comprou a propriedade {player_positons[player.name]} : {output} \n')
                if not output:
                    if property.owner != None:
                        player.balance -= property.rental
                        print(f'\n -> pagou aluguél de : {property.rental} \n')
                print(f'\n {player} \n')
                print(f'\n -> {player.name} ficou com saldo de : {round(player.balance,2)} \n')
                print(f'@@@@@')
            print(f'#####')