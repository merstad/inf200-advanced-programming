"""
Run

   python setup.py build_ext --inplace

to build the Cython modules in this directory and make them available for import.

See also https://cython.readthedocs.io/en/latest/src/quickstart/build.html.
"""


from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Primes Demo',
    ext_modules=cythonize('*.pyx', compiler_directives={'language_level': 3}),
    zip_safe=False
)
