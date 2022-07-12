import os
from src.applications.use_cases.game_round import GameRound
from src.domain.entities.property import Property
from src.domain.entities.player import *


if __name__ == '__main__':

    simulations = int(os.environ.get('SIMULATIONS', 0))
    rounds = int(os.environ.get('ROUNDS', 0))

    for i in range(simulations):
        properties = []
        for i in range(20):
            price = round(random.uniform(100_000.00, 250_000.00), 2)
            rental = round(random.uniform(1000.00, 10_000.00), 2)
            properties.append(Property(price=price, rental=rental))
        players = [
            PlayerInpulsive("Player Inpulsive"),
            PlayerPicky("Player Picly"),
            PlayerCautious("Player Cautious"),
            PlayerRandom("Player Randon")

        ]
        game_round = GameRound(properties, players)
        game_round.execute(rounds)