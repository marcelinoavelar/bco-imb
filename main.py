import argparse
import secrets

from src.applications.use_cases.game_round import GameRound
from src.domain.entities.property import Property
from src.domain.entities.player import *


def get_parser():
    parser = argparse.ArgumentParser()
    parser_group = parser.add_argument_group()
    parser_group.add_argument('-s', '--simulations', dest='simulations', type=int, required=True,
                              help='Quantiade de simuações')
    parser_group.add_argument('-d', '--rounds', dest='rounds',
                              type=int, required=True,
                              help='Quantidades de rodadas')
    parser_group.add_argument('-x', '--min_price', dest='min_price', type=float, required=True,
                              help='Valor minimo para geração randomica de preço das propriedades')
    parser_group.add_argument('-p', '--max_price', dest='max_price', type=float, required=True,
                              help='Valor maximo para geração randomica de preço das propriedades')
    parser_group.add_argument('-r', '--min_rental', dest='min_rental', type=float, required=True,
                              help='Valor minimo para geração randomica de aluguel das propriedades')
    parser_group.add_argument('-t', '--max_rental', dest='max_rental', type=float, required=True,
                              help='Valor maximo para geração randomica de aluguel das propriedades')
    parser_group.add_argument('-c', '--game_properties', dest='game_properties', type=int, required=True,
                              help='Quantidade de propriedades')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_parser()
    simulations = args.simulations
    rounds = args.rounds
    min_price = args.min_price
    max_price = args.max_price
    min_rental = args.min_rental
    max_rental = args.max_rental
    game_properties = args.game_properties

    for i in range(simulations):
        properties = []
        for i in range(game_properties):
            price = round(random.uniform(min_price, max_price), 2)
            rental = round(random.uniform(min_rental, max_rental), 2)
            property = Property(price=price, rental=rental)
            if round(random.uniform(1, 3)) == 2:
                property.purchase(secrets.token_urlsafe(6))
            properties.append(property)

        players = [
            PlayerInpulsive("Player Inpulsive"),
            PlayerPicky("Player Picly"),
            PlayerCautious("Player Cautious"),
            PlayerRandom("Player Randon")
        ]
        game_round = GameRound(properties, players)
        output = game_round.execute(rounds)
        print(f'\n -> {output} ')
