# distutils: language = c++
# distutils: sources = cpp_primes.cpp

"""
Cython wrapper around pure C++ version.

Note: the #distutils lines above must be at the very top of this file.
"""


from libcpp.vector cimport vector

cdef extern from "cpp_primes.h":
    vector[int] cpp_primes(int n_primes)

cpdef primes(n_primes):
    return cpp_primes(n_primes)
