"""
Example solution for Deliverable 3 with challenge.

This module provides a complex number class.
"""

__author__ = "Hans Ekkehard Plesser / NMBU"


import math


class Complex:
    """
    Complex number class supporting cartesian and polar coordinates.
    """

    # * in argument list means r and phi must be given as named parameters
    def __init__(self, re=None, im=None, *, r=None, phi=None):
        """
        Complex numbers can be created in the following ways:

        Complex()     -> 0 + 0i
        Complex(1)    -> 1 + 0i
        Complex(im=1) -> 0 + 1i
        Complex(1, 2) -> 1 + 2i
        Complex(r=1)  -> 1 + 0i
        Complex(r=1, phi=2) -> 1 * exp(2i)
        """

        cart = re is not None or im is not None
        polar = r is not None or phi is not None

        if cart and polar:
            raise ValueError('Cannot mix cartesian and polar coordinates.')
        if polar and r is None:
            raise ValueError('Polar coordinates require absolute value r.')

        if cart:
            self.re = re if re else 0
            self.im = im if im else 0
            self.r = math.sqrt(self.re ** 2 + self.im ** 2)
            self.phi = math.atan2(self.im, self.re)
        elif polar:
            self.r = r
            self.phi = phi if phi else 0
            self.re = self.r * math.cos(self.phi)
            self.im = self.r * math.sin(self.phi)
        else:  # no arguments given
            self.re = self.im = self.r = self.phi = 0

    @property
    def conj(self):
        return Complex(self.re, -self.im)

    def __repr__(self):
        return f"Complex({self.re}, {self.im})"

    def __str__(self):
        return f"{self.re}{self.im:+}i"

    def __eq__(self, rhs):
        return self.re == rhs.re and self.im == rhs.im
    
    def __ne__(self, rhs):
        return not self == rhs
    
    def __neg__(self):
        return Complex(-self.re, -self.im)

    def __add__(self, rhs):
        # allow adding non-complex numbers
        try:
            return Complex(self.re + rhs.re, self.im + rhs.im)
        except AttributeError:
            return Complex(self.re + rhs, self.im)

    def __radd__(self, lhs):
        return self + lhs

    def __sub__(self, rhs):
        # map to __neg__ and __add__
        return self + (-rhs)

    def __rsub__(self, lhs):
        return Complex(lhs) - self

    def __mul__(self, rhs):
        # allow multiplication by non-complex number
        try:
            return Complex(self.re*rhs.re-self.im*rhs.im,
                           self.re*rhs.im+self.im*rhs.re)
        except AttributeError:
            return Complex(self.re * rhs, self.im * rhs)

    def __rmul__(self, lhs):
        return self * lhs

    def __truediv__(self, rhs):
        # Division of complex by complex can only easily be expressed in polar coordinates
        try:
            return Complex(r=self.r/rhs.r, phi=self.phi-rhs.phi)
        except AttributeError:
            return Complex(self.re / rhs, self.im / rhs)

    def __rtruediv__(self, lhs):
        # Division of real number by complex
        return lhs * self**(-1)

    def __pow__(self, rhs):
        try:
            # Exponentiation requires polar and cartesian coordinates
            r, phi = self.r, self.phi
            c, d = rhs.re, rhs.im
            if r == 0:
                if rhs.r == 0:
                    return Complex(1)   # 0^0 == 1 by definition
                elif c > 0:
                    return Complex(0)   # 0^(c + di) == 0 if c > 0
                else:
                    raise ValueError('Undefined value.')
            return Complex(r=r**c * math.exp(-phi * d),
                           phi=c*phi + d*math.log(r))
        except AttributeError:
            # Exponent is scalar. Convert to Complex rhs + 0i and try again.
            return self**Complex(rhs)

    def __rpow__(self, lhs):
        # Raise scalar to complex power
        return Complex(lhs)**self
