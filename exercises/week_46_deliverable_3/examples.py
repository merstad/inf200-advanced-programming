"""
Examples for Complex class.
"""

__author__ = "Hans Ekkehard Plesser / NMBU"


from complex import Complex
import math

z = Complex(1, 2)
y = Complex(3, 4)

print(z)
print([z, y])

print(z.re)
print(z.im)

print(Complex())
print(Complex(5))

print("z + y =", z + y)
print("z - y =", z - y)
print("z * y =", z * y)
print("z / y =", z / y)
print("z ^ y =", z ** y)

print("z + 3 =", z + 3)
print("3 + z =", 3 + z)
print("z * 3 =", z * 3)
print("3 * z =", 3 * z)
print("z / 3 =", z / 3)
print("3 / z =", 3 / z)
print("z ^ 3 =", z**3)
print("3 ^ z =", 3**z)

print("z == y:", z == y)
print("z != y:", z != y)

try:
    print(z < y)
except TypeError as err:
    print(err)

z = Complex(r=1, phi=math.pi / 4)
print(z)
print(z.r, z.phi)
print(z.conj)
print(-z)

print("i ^ i =", Complex(0, 1)**Complex(0, 1))
