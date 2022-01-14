"""
Compute Fibonacci numbers recursively with memoization.

See Lecture 11 for details on memoization.
"""


def memoize(func):
    _memo = {}

    def wrapped(arg):
        if arg not in _memo:
            _memo[arg] = func(arg)
        return _memo[arg]

    return wrapped


@memoize
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    res = 0
    for _ in range(100000):
        res = fib(350)
    print(res)
