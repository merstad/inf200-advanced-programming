"""
A minimal and meaningless example program to illustrate profiling.
"""


def h(n):
    return n**10


def f(k):
    s = 0
    for n in range(k):
        s += h(n)
    return s


if __name__ == '__main__':
    x = f(100000)
    print(x)
