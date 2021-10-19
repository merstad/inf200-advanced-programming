"""
Various implementations of the Sieve of Erastosthenes.
"""

__author__ = "Hans Ekkehard Plesser / NMBU"

import numpy as np


def sieve_list(n):
    """
    Implementation based on a Python list.

    :param n: Largest number to test for primality.
    :return: List of primes up to and including n.
    """

    # Create list of all numbers from 2..n, our candidates for primality
    primes = [k for k in range(2, n+1)]

    # Test all divisors from 2 up to the square root of n
    d = 2
    while d**2 <= n:
        # Keep only the divisor d and numbers not divisible by d
        primes = [k for k in primes if k == d or k % d != 0]

        # The next divisor we need to test is the smallest number in primes
        # larger than the current divisor.
        d = min(k for k in primes if k > d)

    return primes


def sieve_set(n):
    """
    Solution using Python sets.
    """

    # Set of candidate primes up to n
    primes = set(range(2, n + 1))

    # Initialise and loop as above
    d = 2
    while d**2 <= n:
        # Remove from the set of primes the set of multiples of d
        primes -= set(range(d * 2, n + 1, d))

        # Take the smallest number in the set larger than d as new divisor
        d = min(k for k in primes if k > d)

    # Return result as list
    return list(primes)


def sieve_numpy(n):
    """
    Implementation using a NumPy array.
    """

    # Create a NumPy array with n+1 entries representing the numbers
    # from 0 to n. Each position is initialized with 1, indicating that
    # we consider all numbers as candidate primes.
    prime_positions = np.ones(n+1)  # +1: index corresponds to value
    prime_positions[:2] = 0

    # Initialize divisor and loop as above
    d = 2
    while d**2 <= n:
        # Use slicing to set entries for all multiples of d to zero
        prime_positions[(2*d)::d] = 0

        # We obtain the next divisor as follows:
        # - np.nonzero()[0] gives the indices of non-zero entries in prime_positions
        #   beyond d. We want the first one of these.
        #   The [0] is needed due to the way nonzero() works.
        # - nz[0] is then the index of the first non-zero entry beyond d, but counting
        #   from (d+1). We thus increase d by nz[0] + 1.
        nz = np.nonzero(prime_positions[(d+1):])[0]
        d += nz[0] + 1

    # Finally, we extract the indices of all non-zero elements (not multiples of any
    # divisor from 2 upwards and convert to a list.
    nz_final = np.nonzero(prime_positions)[0]
    return list(nz_final)


if __name__ == '__main__':
    for sieve in [sieve_list, sieve_set, sieve_numpy]:
        print(f'{sieve.__name__:11s}: {sieve(40)}')
