"""
Tests for Simulation class.
"""
__author__ = 'Hans E Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'

import pytest

from biolab.simulation import Sim


class TestSimulation:
    """
    Tests for Simulation class.
    """

    @pytest.fixture(autouse=True)
    def create_sim(self):
        self.n_dish = 5
        self.n_a = 10
        self.n_b = 20
        self.sim = Sim(self.n_dish, self.n_a, self.n_b, 12345)

    def test_sim_create(self):
        """
        Test that simulation can be created by just running setup.

        This test is not really necessary, since all other tests would not
        work anyways if the simulation cannot be created. But in a strict
        TDD approach, this test would give us reason to create class
        Simulation.
        """
        assert self.sim

    def test_run_data_shape(self):
        """
        Test that simulation can run at all and returns data of correct shape.
        """

        data = self.sim.run(cycles=0, return_counts=True)
        assert data.shape == (1, 3)

    def test_correct_initial_counts(self):
        """
        Test that simulation is set up with correct number of bacteria.
        """

        data = self.sim.run(cycles=0, return_counts=True)
        cycle, tot_a, tot_b = data[0, :]
        assert (cycle == 0 and
                tot_a == self.n_dish * self.n_a and
                tot_b == self.n_dish * self.n_b)
