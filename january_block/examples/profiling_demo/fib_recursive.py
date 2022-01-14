"""
Recursively comupte Fibonacci numbers.

Note: Run-time grows very rapidly for n > 30.
"""


def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(35))