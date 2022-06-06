"""
Brief illustration of re-plotting vs data-updating.
"""

import matplotlib.pyplot as plt
import numpy as np
import random


def replot(n_steps):
    """
    Naive function plotting a curve one data point at a time.

    This function calls plot() for each new data point added, leading to
    increasingly slower figure updates.

    :param n_steps: number of steps to plot
    """

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, n_steps)
    ax.set_ylim(0, 1)

    data = []
    for _ in range(n_steps):
        data.append(random.random())
        ax.plot(data, 'b-')
        fig.canvas.flush_events()
        plt.pause(1e-6)


def update(n_steps):
    """
    Plot function one point at a time by updating plot data.

    This function calls plot() only once, setting all x-data and filling
    y-data with NaN values. y-data is then updated to add each new data
    point. This avoids slow-down.

    :param n_steps: Number of steps to plot
    """

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, n_steps)
    ax.set_ylim(0, 1)

    line = ax.plot(np.arange(n_steps),
                   np.full(n_steps, np.nan), 'b-')[0]

    for n in range(n_steps):
        ydata = line.get_ydata()
        ydata[n] = random.random()
        line.set_ydata(ydata)
        plt.pause(1e-6)


def update2(n_steps):
    """
    Plot function one point at a time by updating plot data.

    This function calls plot() only once. Data to be plotted is built
    as Python lists, adding one point at a time. At each step, these
    lists are set as x- and y-data, respectively. This avoids slow-down.

    :param n_steps: Number of steps to plot
    """

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(0, n_steps)
    ax.set_ylim(0, 1)

    line = ax.plot([], [], 'b-')[0]

    xdata = []
    ydata = []
    for n in range(n_steps):
        xdata.append(n)
        ydata.append(random.random())
        line.set_xdata(xdata)
        line.set_ydata(ydata)
        plt.pause(1e-6)

if __name__ == '__main__':
    num_steps = 1000

    replot(num_steps)
    # update(num_steps)
    # update2(num_steps)

    plt.show()
