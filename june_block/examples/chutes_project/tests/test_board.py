"""
Tests for Board class.
"""

import pytest

from chutes.board import Board

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'


def test_goal_not_reached():
    """"Ensure goal_reached() does not yield false positives."""
    goal_pos = 20
    brd = Board(ladders=[], chutes=[], goal=goal_pos)
    for pos in range(goal_pos):
        assert not brd.goal_reached(pos)


def test_goal_reached():
    """Ensure goal_reached() does not yield false negatives."""
    goal_pos = 20
    brd = Board(ladders=[], chutes=[], goal=goal_pos)
    for pos in range(goal_pos, goal_pos+10):
        assert brd.goal_reached(pos)


def test_adjust_empty_board():
    """"No position adjustment on empty board."""

    goal_pos = 20
    brd = Board(ladders=[], chutes=[], goal=goal_pos)
    for pos in range(goal_pos):
        assert brd.position_adjustment(pos) == 0


def test_adjustment():
    goal_pos = 20
    ladders = [(2, 10), (9, 13), (12, 18)]
    chutes = [(4, 1), (7, 3), (17, 8)]
    test_cases = {0: 0, 1: 0, 2: 8, 3: 0, 4: -3, 5: 0, 6: 0, 7: -4,
                  8: 0, 9: 4, 10: 0, 11: 0, 12: 6, 13: 0, 14: 0,
                  15: 0, 16: 0, 17: -9, 18: 0, 19: 0}
    brd = Board(ladders=ladders, chutes=chutes, goal=goal_pos)
    for pos, change in test_cases.items():
        assert brd.position_adjustment(pos) == change


@pytest.mark.parametrize("from_pos, to_pos",
                         [[1, 40],
                          [2, 2],
                          [33, 3]])
def test_default_board_adjustments(from_pos, to_pos):
    """Test chutes and ladders on default board."""

    brd = Board()
    assert from_pos + brd.position_adjustment(from_pos) == to_pos


@pytest.mark.parametrize("pos, is_goal",
                         [[89, False],
                          [90, True],
                          [91, True]])
def test_default_board_goal(pos, is_goal):
    """Test goal detection on default board."""

    brd = Board()
    assert brd.goal_reached(pos) == is_goal


@pytest.mark.parametrize('bad_config',
                         [{'ladders': [(10, 10)]},
                          {'ladders': [(10, 9)]},
                          {'chutes': [(10, 10)]},
                          {'chutes': [(9, 10)]},
                          {'goal': 0}])
def test_bad_boards(bad_config):
    """Test that bad board specifications are not accepted."""

    with pytest.raises(ValueError):
        # **bad_config expands the dictionary as parameter=value
        # arguments in constructor call
        Board(**bad_config)
