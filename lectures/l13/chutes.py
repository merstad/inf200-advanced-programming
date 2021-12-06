# -*- coding: utf-8 -*-

"""
A simulation of the Chutes & Ladders game.
"""

import random
import numpy

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'

CHUTES_AND_LADDERS = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70,
                      1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
GOAL = 90


def single_game(num_players):
    """
    Returns duration of single game.

    :param num_players: number of players in game
    :return: number of moves the winning player needed to reach the goal
    """

    positions = [0] * num_players
    num_moves = 0

    while max(positions) < GOAL:
        for player in range(num_players):
            positions[player] += random.randint(1, 6)
            if positions[player] in CHUTES_AND_LADDERS:
                positions[player] = CHUTES_AND_LADDERS[positions[player]]
        num_moves += 1

    return num_moves


def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    :param num_games: number of games to play
    :param num_players: number of players in each game
    :return: sequence with number of moves needed in each game
    """

    return [single_game(num_players) for _ in range(num_games)]


def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    :param num_games: number of games to play
    :param num_players: number of players in each game
    :param seed: random number seed for experiment
    :return: sequence with number of moves needed in each game
    """

    random.seed(seed)
    return multiple_games(num_games, num_players)


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    s_data = sorted(data)
    n = len(s_data)
    return (s_data[n // 2] if n % 2 == 1
            else 0.5 * (s_data[n // 2 - 1] + s_data[n // 2]))


if __name__ == '__main__':
    number_of_games = 100
    number_of_players = 4
    random_seed = 1233415

    number_of_moves = multi_game_experiment(number_of_games, number_of_players,
                                            random_seed)

    print('Shortest game: {:3d} moves'.format(min(number_of_moves)))
    print('Median game  : {:5.1f} moves'.format(median(number_of_moves)))
    print('Longest game : {:3d} moves'.format(max(number_of_moves)))
    print('Average game : {:5.1f} +- {:.1f} moves'.format(
                    numpy.mean(number_of_moves), numpy.std(number_of_moves)))
