from distutils.core import setup, Extension

setup(
    name = 'oset', 
    version = '1.0',
    ext_modules = [
        Extension('oset', 
                  ['oset.3.cpp'], 
                  language='c++',
                  extra_compile_args=['-std=c++11'])
    ]
)