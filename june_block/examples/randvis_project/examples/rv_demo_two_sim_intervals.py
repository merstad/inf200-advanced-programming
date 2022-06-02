#!/usr/bin/env python

"""
This is a small demo script running a randvis simulation.

The simulation is split into two intervals to illustrate the
extension of the x-axis in line plots.
"""

import matplotlib.pyplot as plt
from randvis.simulation import DVSim

if __name__ == '__main__':

    sim = DVSim((10, 15), 0.1, 12345)
    sim.simulate(50, 1, 5)

    input('Press ENTER to simulate some more!')

    sim.simulate(150, 1, 5)

    print('Close the figure to end the program!')

    plt.show()
