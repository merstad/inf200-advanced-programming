import math
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def __add__(self, rhs):
        return Vector(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, rhs):
        return Vector(self.x * rhs, self.y * rhs)

    def __rmul__(self, lhs):
        return self * lhs

    def __truediv__(self, rhs):
        return self * (1. / rhs)

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
