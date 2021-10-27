# -*- coding: utf-8 -*-

"""
Exercise 02-D: Evaluating polynomials using Horner's rule

Part of a course at Norges miljø- og biovitenskapelige universitet på Ås.
"""

__author__ = 'Hans Ekkehard Plesser'
__email__ = 'hans.ekkehard.plesser@nmbu.no'


def p(a, x):
    """
    Evaluate polynomial using Horner's rule.

    :param a: Polynomial coefficients, a[0]=a_0, a[-1]=a_n; list-like
    :param x: Value for which to evaluate polynomial; scalar
    :returns: Value of polynomial at x
    """

    y = a[-1]
    for c in a[-2::-1]:
        y = c + x * y

    return y


if __name__ == '__main__':

    print('{:>20s}{:>10s}{:>10s}{:>10s}'.format('Polynomial', 'x', 'Expected', 'Computed'))

    tfmt = '{:>20s}{:10.3f}{:10.3f}{:10.3f}'
    print(tfmt.format('4', 0, 4, p([4], 0)))
    print(tfmt.format('3x^2-2x+5', 0, 5, p([5, -2, 3], 0)))
    print(tfmt.format('3x^2-2x+5', 1, 6, p([5, -2, 3], 1)))
    print(tfmt.format('3x^2-2x+5', 0.5, 4.75, p([5, -2, 3], 0.5)))
    print(tfmt.format('x^10+3', 2, 1027, p([3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 2)))
