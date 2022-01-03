"""
Tests for Player class.
"""

import random

from chutes.player import Player
from chutes.board import Board

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'


def test_single_step_one(mocker):
    """
    Use mocked randint to test that a player makes a correct initial step
    of length step_size.
    """

    step_size = 1

    # the next line replaces random.randint with a mock function
    # returning step_size for the rest of this test.
    mocker.patch('random.randint', return_value=step_size)

    b = Board(chutes=[], ladders=[])
    pl = Player(b)
    pl.move()
    assert pl.position == step_size


def test_multi_step_three(mocker):
    """
    Use mocked randint to test that player makes multiple moves
    of given length.
    """

    n_steps = 5
    randint_value = 3

    # Patch random.randint to always return randint_value
    mocker.patch('random.randint', return_value=randint_value)

    # Wrap a "spy" around random.randint to collect information about
    # how often and with which arguments it is called.
    randint_spy = mocker.spy(random, 'randint')

    b = Board(chutes=[], ladders=[])
    pl = Player(b)
    for _ in range(n_steps):
        pl.move()

    # Check that player is in correct position
    assert pl.position == n_steps * randint_value

    # Check that random.randint was called once per call to move()
    assert randint_spy.call_count == n_steps

    # Check that random.randint was always called with arguments 1, 6
    randint_spy.assert_has_calls(n_steps * [mocker.call(1, 6)])
