from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    name = 'primes', 
    version = '1.0',
    ext_modules = cythonize('primes.pyx')
)