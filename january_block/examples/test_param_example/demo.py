"""
This module provides a minimal class hierarchy to illustrate test parameterization.
"""


class A:
    def __init__(self):
        self.x = 0
        self.s = None

    def step(self):
        self.x += self.s


class B(A):
    def __init__(self):
        super().__init__()
        self.s = 1


class C(A):
    def __init__(self):
        super().__init__()
        self.s = 2


if __name__ == "__main__":
    b = B()
    c = C()
    b.step()
    c.step()
    print(b.x)
    print(c.x)

