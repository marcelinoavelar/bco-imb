import argparse
import secrets
import operator
import json
from textwrap import indent
from src.applications.use_cases.game_round import GameRound
from src.domain.entities.property import Property
from src.domain.entities.player import *


def get_parser():
    parser = argparse.ArgumentParser()
    parser_group = parser.add_argument_group()
    parser_group.add_argument('-s', '--simulations', dest='simulations', type=int, required=True,
                              help='Number of simulations')
    parser_group.add_argument('-d', '--rounds', dest='rounds',
                              type=int, required=True,
                              help='Number of rounds')
    parser_group.add_argument('-x', '--min_price', dest='min_price', type=float, required=True,
                              help='Minimum value for random property price generation')
    parser_group.add_argument('-p', '--max_price', dest='max_price', type=float, required=True,
                              help='Maximum value for random property price generation')
    parser_group.add_argument('-r', '--min_rental', dest='min_rental', type=float, required=True,
                              help='Minimum value for random generation of rental properties')
    parser_group.add_argument('-t', '--max_rental', dest='max_rental', type=float, required=True,
                              help='Maximum value for random generation of rental properties')
    parser_group.add_argument('-c', '--game_properties', dest='game_properties', type=int, required=True,
                              help='Number of properties')
    return parser.parse_args()


def get_winners_percent_by_profile(winners: list) -> list:
    winners_percente = dict({})
    for winner in winners:
        winners_percente[winner] = round(int(winners[winner])/300*100, 2)
    return winners_percente


def get_top_winner(winners: list) -> str:
    winners = sorted(winners.items(), key=operator.itemgetter(1), reverse=True)
    winners = {k: v for k, v in winners}
    return list(winners.keys())[0]


if __name__ == '__main__':
    args = get_parser()
    simulations = args.simulations
    rounds = args.rounds
    min_price = args.min_price
    max_price = args.max_price
    min_rental = args.min_rental
    max_rental = args.max_rental
    game_properties = args.game_properties

    round_end_per_timeout = 0
    count_rounds = 0
    winner_ranking = dict({})

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

        round_end_per_timeout += int(output.get('timeout', ''))
        count_rounds += int(output.get('rounds', ''))

        try:
            winner_ranking[output.get('winner', '')] += 1
        except:
            winner_ranking[output.get('winner', '')] = 1

    result = {
        "round_end_per_timeout": round_end_per_timeout,
        "average_rounds_per_game": round(count_rounds/simulations, 2),
        "winners_percent_by_profile": get_winners_percent_by_profile(winner_ranking),
        "top winner": get_top_winner(winner_ranking)
    }
    result_json = json.dumps(result, indent=2)
    print(result_json)
