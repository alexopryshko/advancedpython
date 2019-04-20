from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    name = 'fib', 
    version = '1.0',
    ext_modules = cythonize('fib.pyx')
)



