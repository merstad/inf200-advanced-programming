"""
Tests illustrating how to parameterize tests with classes.

The overall aim here is to perform the same tests on two different
classes which are subclasses of a common superclass.
"""

import pytest
from demo import B, C


@pytest.mark.parametrize('class_to_test', [B, C])
def test_step_increases_x(class_to_test):
    """
    Test that stepping increases the position x.

    :param class_to_test: The class for which the test is to be performed
    """

    obj = class_to_test()   # create class instance
    x_orig = obj.x
    obj.step()
    assert obj.x > x_orig


@pytest.mark.parametrize('class_to_test, expected_step', [(B, 1),
                                                          (C, 2)])
def test_step_correct_increase(class_to_test, expected_step):
    """
    Test that stepping changes the position correctly.

    :param class_to_test: Class for which to apply test
    :param expected_step: Step size for given class
    """

    obj = class_to_test()
    x_orig = obj.x
    obj.step()
    assert obj.x == x_orig + expected_step


@pytest.mark.parametrize('class_to_test', [B, C])
@pytest.mark.parametrize('num_steps', [0, 1, 10, 50])
def test_multiple_steps(class_to_test, num_steps):
    """
    Test that repeated calls to step() work correctly.

    This test illustrates how parameterization along two dimensions can
    be combined.

    :param class_to_test: Class for which the test is to be performed
    :param num_steps: Number of times to call step()
    """
    obj = class_to_test()
    x_orig = obj.x
    step_size = obj.s
    for _ in range(num_steps):
        obj.step()
    assert obj.x == x_orig + num_steps * step_size
