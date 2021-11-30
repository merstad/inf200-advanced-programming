"""
Unit tests for Complex class
"""

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'

import math
import pytest

from complex import Complex


@pytest.mark.parametrize("args, re, im",
                         [((), 0, 0),
                          ((5,), 5, 0),
                          ((0, 4), 0, 4),
                          ((3, 4), 3, 4)])
def test_init_cart(args, re, im):
    """Test for cartesian initialization of complex numbers."""

    z = Complex(*args)
    assert z.re == re and z.im == im


@pytest.mark.parametrize("kwargs, re, im",
                         [({'r': 0}, 0, 0),
                          ({'r': 1, 'phi': 0}, 1, 0),
                          ({'r': 2, 'phi': math.pi}, -2, 0),
                          ({'r': 2, 'phi': math.pi/2}, 0, 2)])
def test_init_polar(kwargs, re, im):
    """Test for polar initialization of complex numbers."""

    z = Complex(**kwargs)
    assert z.re == pytest.approx(re) and z.im == pytest.approx(im)


def test_polar_requires_r():
    """Polar specification must include absolute value"""

    with pytest.raises(ValueError):
        Complex(phi=0)


@pytest.mark.parametrize("args, kwargs",
                         [((0, 1), {'r': 1, 'phi': 2}),
                          ((1,), {'r': 2}),
                          ((), {'im': 1, 'phi': 2})])
def test_prohibit_cartesian_polar_mix(args, kwargs):
    """Ensure mix of cartesian and polar coordinates is detected."""
    with pytest.raises(ValueError):
        Complex(*args, **kwargs)


@pytest.mark.parametrize("re, im",
                         [(0, 0),
                          (1, 0),
                          (0, 2),
                          (3, 4),
                          (-5, -2)])
def test_modulus(re, im):
    """Test for absolute value (modulus) of the complex number."""

    z = Complex(re, im)
    r = math.sqrt(re**2 + im**2)
    assert z.r == pytest.approx(r)


@pytest.mark.parametrize("re, im, phi",
                         [(0, 0, 0),
                          (1, 0, 0),
                          (0, 1, math.pi/2),
                          (-2, 2, 3/4*math.pi),
                          (1, -1, -math.pi/4)])
def test_arg(re, im, phi):
    """Test for argument/angle of the complex number"""

    z = Complex(re, im)
    assert z.phi == pytest.approx(phi)


@pytest.mark.parametrize("re, im",
                         [(0, 0),
                          (1, 0),
                          (0, 2),
                          (3, 4),
                          (-5, -2)])
def test_conjugate(re, im):
    """Test for conjugate of the complex number"""

    zc = Complex(re, im).conj
    assert zc.re == re and zc.im == -im


@pytest.mark.parametrize("re, im, c_str",
                         [(0, 0, '0+0i'),
                          (1, 0, '1+0i'),
                          (0, 2, '0+2i'),
                          (3, 4, '3+4i'),
                          (-5, -2, '-5-2i')])
def test_print(re, im, c_str):
    """Test correct string representation."""

    assert str(Complex(re, im)) == c_str


@pytest.mark.parametrize("re, im",
                         [(0, 0),
                          (1, 0),
                          (0, 2),
                          (3, 4),
                          (-5, -2)])
def test_represent(re, im):
    """Test for representation of the object"""

    assert repr(Complex(re, im)) == f'Complex({re}, {im})'


@pytest.mark.parametrize("left, right, expected",
                         [(Complex(1, 2), Complex(1, 2), True),
                          (Complex(1, 2), Complex(2, 1), False),
                          (Complex(r=1, phi=1), Complex(r=1, phi=1), True),
                          (Complex(r=1, phi=1), Complex(r=1, phi=2), False),
                          (Complex(2, 0), Complex(r=2, phi=0), True)])
def test_equality(left, right, expected):
    """Test for equality operator"""

    result = left == right
    assert result == expected


@pytest.mark.parametrize("left, right, expected",
                         [(Complex(1, 2), Complex(1, 2), False),
                          (Complex(1, 2), Complex(2, 1), True),
                          (Complex(r=1, phi=1), Complex(r=1, phi=1), False),
                          (Complex(r=1, phi=1), Complex(r=1, phi=2), True),
                          (Complex(2, 0), Complex(r=2, phi=0), False)])
def test_unequal(left, right, expected):
    """Test for inequality operator"""

    result = left != right
    assert result == expected


@pytest.mark.parametrize("compare",
                         [lambda x, y: x < y,
                          lambda x, y: x <= y,
                          lambda x, y: x > y,
                          lambda x, y: x >= y])
def test_undefined_comparisons(compare):
    """Test that all comparison except equal and unequal are undefined."""

    with pytest.raises(TypeError):
        compare(Complex(1, 2), Complex(3, 4))


@pytest.mark.parametrize("re, im",
                         [(0, 0),
                          (1, 0),
                          (0, 2),
                          (3, 4),
                          (-5, -2)])
def test_negation(re, im):
    """Test for negation of a  complex number"""

    z = -Complex(re, im)
    assert z.re == -re and z.im == -im


@pytest.mark.parametrize("lhs, rhs, expected",
                         [(Complex(1.3123, 3), Complex(2, 3), Complex(3.3123, 6)),
                          (Complex(0, 41.2), Complex(45, 0), Complex(45, 41.2)),
                          (Complex(2, 3), 5, Complex(7.00, 3)),
                          (2.00, Complex(45, 0), Complex(47, 0))])
def test_addition(lhs, rhs, expected):
    """
    Test addition of a complex number with a real/complex number,
    on different sides of operator
    """

    assert lhs + rhs == expected


@pytest.mark.parametrize("lhs, rhs, expected",
                         [(Complex(1.3125, 3), Complex(2, 3), Complex(-0.6875, 0)),
                          (Complex(0, 41.2), Complex(45, 0), Complex(-45, 41.2)),
                          (Complex(2, 3), 5, Complex(-3, 3)),
                          (2.00, Complex(45, 0), Complex(-43, 0))])
def test_subtraction(lhs, rhs, expected):
    """
    Test addition of a complex number with a real/complex number,
    on different sides of operator
    """

    assert lhs - rhs == expected


@pytest.mark.parametrize("lhs, rhs, expected",
                         [(Complex(1, 3), Complex(2, -2), Complex(8, 4)),
                          (Complex(0, 0.5), Complex(0.5, 0), Complex(0, 0.25)),
                          (Complex(2, 3), 5, Complex(10, 15)),
                          (2.00, Complex(45, 7.2), Complex(90, 14.4))])
def test_multiplication(lhs, rhs, expected):
    """
    Test multiplication of complex number with a real/complex number,
    on different sides of operator
    """

    assert lhs * rhs == expected


@pytest.mark.parametrize("lhs, rhs, expected",
                         [(Complex(1, 3), 2, Complex(0.5, 1.5)),
                          (1, Complex(r=2, phi=math.pi), Complex(r=0.5, phi=-math.pi)),
                          (Complex(2, 5), Complex(2, 5), Complex(1, 0)),
                          (Complex(r=4, phi=math.pi), Complex(r=2, phi=math.pi/2),
                           Complex(r=2, phi=math.pi/2))])
def test_division(lhs, rhs, expected):
    """
    Test division of complex number by a real/complex number,
    on different sides of operator
    """

    z = lhs / rhs
    assert z.re == pytest.approx(expected.re) and z.im == pytest.approx(expected.im)


@pytest.mark.parametrize("lhs, rhs, expected",
                         [(Complex(0, 1), 2, Complex(-1, 0)),
                          (1, Complex(r=2, phi=math.pi), Complex(1, 0)),
                          (Complex(), Complex(), Complex(1, 0)),  # 0^0 = 1
                          (Complex(), 2, Complex()),  # 0^2 = 0
                          (Complex(0, 1), Complex(0, 1), Complex(math.exp(-math.pi/2), 0))])
def test_power(lhs, rhs, expected):
    """
    Test exponentiation of complex number by a real/complex number,
    on different sides of operator
    """

    z = lhs**rhs
    assert z.re == pytest.approx(expected.re) and z.im == pytest.approx(expected.im)


def test_power_exception():
    """
    Test that exception is raised for undefined power.
    """

    with pytest.raises(ValueError):
        Complex()**Complex(-1, 2)
