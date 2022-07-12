from src.applications.use_cases.game_round import GameRound
from src.domain.entities.property import Property
from src.domain.entities.player import *


if __name__ == '__main__':
    properties = []
    for i in range(20):
        price = round(random.uniform(100.00, 350.00), 2)
        rental = round(random.uniform(2.00, 20.00), 2)
        properties.append(Property(price=price, rental=rental))
    players = [
        PlayerInpulsive("Player Inpulsive"),
        PlayerPicky("Player Picly"),
        PlayerCautious("Player Cautious"),
        PlayerRandom("Player Randon")

    ]
    game_round = GameRound(properties, players)
    game_round.execute()
