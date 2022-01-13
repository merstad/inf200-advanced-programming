"""
Tests illustrating how to combine parameterization of classes with other parameterization.
"""

import pytest
from demo import B, C


@pytest.mark.parametrize('class_to_test', [B, C])
class TestDemo:
    """
    A set of tests that can be applied equally to classes B and C.

    This class of tests illustrates how you can combine parameterization
    along two dimensions. The class itself is parameterized with the
    subclass to be tested (class B or C from module demo), while the
    test_multiple_steps() method is parameterized with different numbers
    of steps. PyTest will run all possible combinations.

    The parameterization variable "class_to_test" can be passed to any
    method defined in this class.

    Note that the tests themselves should be designed so that the
    expected solution can be determined just on the basis of the parameters,
    since it would be difficult to provide expected results explicitly
    for each combination of class_to_test and num_steps.
    """

    def test_step_increases_x(self, class_to_test):
        """
        Test that stepping increases the position x.

        :param class_to_test: The class for which the test is to be performed
        """

        obj = class_to_test()
        x_orig = obj.x
        obj.step()
        assert obj.x > x_orig

    @pytest.mark.parametrize('num_steps', [0, 1, 10, 50])
    def test_multiple_steps(self, class_to_test, num_steps):
        """
        Test that repeated calls to step() work correctly.

        :param class_to_test: Class for which the test is to be performed
        :param num_steps: Number of times to call step()
        """
        obj = class_to_test()
        x_orig = obj.x
        step_size = obj.s
        for _ in range(num_steps):
            obj.step()
        assert obj.x == x_orig + num_steps * step_size
