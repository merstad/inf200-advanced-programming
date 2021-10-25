import random
import matplotlib.pyplot as plt
import numpy as np


def adjust_position(position):
    chutes_and_ladders = {1: 12,
                          13: 22,
                          14: 3,
                          20: 8}
    if position in chutes_and_ladders:
        return chutes_and_ladders[position]
    else:
        return position


def goal_reached(position):
    return position >= 25


def move_player(player_rec):
    player_rec["position"] += random.randint(1, 6)
    player_rec["position"] = adjust_position(player_rec["position"])
    player_rec["steps"] += 1


def one_game():
    player = {"steps": 0, "position": 0}
    while not goal_reached(player["position"]):
        move_player(player)
    return player["steps"]


if __name__ == "__main__":
    random.seed(12345678)
    results = [one_game() for _ in range(1000)]


    print(f'Shortest game duration: {min(results):4d}')
    print(f'Mean game duration    : {np.mean(results):6.1f} ± {np.std(results):.1f}')
    print(f'Longest game duration : {max(results):4d}')

    hv, hb = np.histogram(results, bins=np.arange(0, max(results)))
    plt.step(hb[:-1], hv)
    plt.show()
