import random
import matplotlib.pyplot as plt
import numpy as np


class Board:
    def __init__(self):
        self.chutes_and_ladders = {1: 12,
                                   13: 22,
                                   14: 3,
                                   20: 8}
        self.goal = 25

    def goal_reached(self, position):
        return position >= self.goal

    def adjust_position(self, position):
        if position in self.chutes_and_ladders:
            return self.chutes_and_ladders[position]
        else:
            return position


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
    def __init__(self, number_of_players):
        self.board = Board()
        self.n_players = number_of_players

    def play(self):
        players = [Player(self.board) for _ in range(self.n_players)]
        while not any(self.board.goal_reached(player.position) for player in players):
            for player in players:
                player.move()
        return player.steps


class Experiment:
    def __init__(self, seed, num_games):
        self.seed = seed
        self.num_games = num_games
        self.results = None

        random.seed(self.seed)

    def run(self):
        self.results = [Game().play() for _ in range(self.num_games)]


if __name__ == "__main__":

    for seed in [123455, 324342, 21213, 234234234,  234234,  2342232, 323]:
        test = Experiment(seed, 100)
        test.run()

        print(f'Seed                  : {test.seed:10d}')
        print(f'Shortest game duration: {min(test.results):4d}')
        print(f'Mean game duration    : {np.mean(test.results):6.1f} ± {np.std(test.results):.1f}')
        print(f'Longest game duration : {max(test.results):4d}')
        print()

        hv, hb = np.histogram(test.results, bins=np.arange(0, max(test.results)))
        plt.step(hb[:-1], hv)

    plt.show()
