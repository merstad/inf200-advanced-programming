"""
Chutes and ladders implementation providing boards with different goal-passing rules.

THIS VERSION IS NOT WORKING CORRECTLY!

See recording of INF200 lecture 1 Nov 2021 for details.
"""

__author__ = "Hans Ekkehard Plesser / NMBU"


import random
import matplotlib.pyplot as plt
import numpy as np
import yaml


class Board:

    def __init__(self, goal=25, chutes_and_ladders=None, board_file=None):
        if board_file is not None:
            specs = yaml.safe_load(open(board_file))
            self.goal = specs['goal']
            self.chutes_and_ladders = {**specs['chutes'], **specs['ladders']}
        else:
            self.goal = goal
            if chutes_and_ladders is None:
                self.chutes_and_ladders = {1: 12, 13: 22, 14: 3, 20: 8}
            else:
                self.chutes_and_ladders = chutes_and_ladders

    def description(self):
        """
        Board description as number of chutes and of ladders and goal position.

        :return: String describing board layout.
        """

        # For every start-end pair representing a chute, the comparison start > end
        # is True, for each ladder pair it is False. When summing over True/False values,
        # True counts as 1 and False as 0, so we obtain the number of chutes.
        n_chutes = sum(start > end for start, end in self.chutes_and_ladders.items())
        n_ladders = len(self.chutes_and_ladders) - n_chutes

        return f"{n_chutes} chutes, {n_ladders} ladders, goal {self.goal}"

    def goal_reached(self, position):
        return position >= self.goal

    def valid_position(self, position):
        return True

    def adjust_position(self, position):
        if position in self.chutes_and_ladders:
            return self.chutes_and_ladders[position]
        else:
            return position


class BlockingBoard(Board):

    def valid_position(self, position):
        return position <= self.goal


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0
        self.steps = 0

    def move(self):
        self.position += random.randint(1, 6)
        self.position = self.board.adjust_position(self.position)
        self.steps += 1


class Game:
    def __init__(self, number_of_players=1, board=None):
        if board is None:
            self.board = Board()
        else:
            self.board = board
        self.n_players = number_of_players

    def play(self):
        players = [Player(self.board) for _ in range(self.n_players)]
        while not any(self.board.goal_reached(player.position) for player in players):
            for player in players:
                player.move()
        return players[0].steps


class Experiment:
    def __init__(self, seed, num_games, num_players, board):
        self.seed = seed
        self.num_games = num_games
        self.num_players = num_players
        self.board = board
        self.results = None

        random.seed(self.seed)

    def run(self):
        self.results = [Game(self.num_players, self.board).play() for _ in range(self.num_games)]


if __name__ == "__main__":

    for brd in [Board(), BlockingBoard()]:
        test = Experiment(12345, 1000, 1, brd)
        test.run()

        print(f'Board                 : {test.board.description()}')
        print(f'Shortest game duration: {min(test.results):4d}')
        print(f'Mean game duration    : {np.mean(test.results):6.1f} ± {np.std(test.results):.1f}')
        print(f'Longest game duration : {max(test.results):4d}')
        print()

        hv, hb = np.histogram(test.results, bins=np.arange(0, max(test.results)))
        plt.step(hb[:-1], hv, label=test.board.description())

    plt.legend()
    plt.title('Game duration distribution for different boards')
    plt.xlabel('Number of steps to goal')
    plt.ylabel('Number of games')

    plt.show()
