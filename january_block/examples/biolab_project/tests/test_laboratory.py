"""
Tests for the Laboratory class.
"""

__author__ = 'Hans E Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'

from biolab.laboratory import Lab
from biolab.dish import Dish
from biolab.bacteria import Bacteria


def test_lab_create():
    n_dish = 5
    n_a = 10
    n_b = 20
    lab = Lab(n_dish, n_a, n_b)
    tot_a, tot_b = lab.bacteria_counts()

    assert tot_a == n_dish * n_a and tot_b == n_dish * n_b


def test_dish_aging_call_count(mocker):
    """Test that aging() is called as often as number of Dishes."""

    n_dish = 5
    n_a = 10
    n_b = 20
    lab = Lab(n_dish, n_a, n_b)

    mocker.spy(Dish, "aging")
    lab.cycle()
    # noinspection PyUnresolvedReferences
    assert Dish.aging.call_count == n_dish


def test_bacteria_ages_call_count_poor_example(mocker):
    """
    Test that Bacteria's ages() method is called correct number of times.

    In a given cycle, ages() should be called once per Bacteria in the
    laboratory.

    NOTE:
        This test is a **poor example** (antipattern) of how to design tests.
        The Laboratory class never interacts directly with the Bacteria class,
        but we introduce here, in the test set for the Laboratory class, a
        dependency on the Bacteria class. This will make any further changes
        to the code unnecessarily complex and should therefore be avoided.
    """
    n_dish = 5
    n_a = 10
    n_b = 20
    lab = Lab(n_dish, n_a, n_b)

    mocker.spy(Bacteria, "ages")
    lab.cycle()
    # noinspection PyUnresolvedReferences
    assert Bacteria.ages.call_count == n_dish * (n_a + n_b)
