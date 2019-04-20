from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    name = 'mod1', 
    version = '1.0',
    ext_modules = cythonize('mod1.pyx')
)



