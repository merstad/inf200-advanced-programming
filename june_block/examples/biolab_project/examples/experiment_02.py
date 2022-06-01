#! /usr/bin/env python

"""
An minimal example of a BioLab simulation experiment.
"""

from biolab.simulation import Sim

if __name__ == '__main__':

    sim = Sim(n_dishes=50, n_a=100, n_b=200, seed=1234567,
              p_dth=0.05, p_div=0.05)
    sim.run(cycles=100)
