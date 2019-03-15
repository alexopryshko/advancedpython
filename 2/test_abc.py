import abc
from collections import Hashable, Iterable

# https://github.com/python/cpython/blob/master/Lib/abc.py
# https://github.com/python/cpython/blob/master/Objects/typeobject.c#L3766


class C(abc.ABC):
    @abc.abstractmethod
    def my_abstract_method(self):
        pass

    @classmethod
    @abc.abstractmethod
    def my_abstract_classmethod(cls):
        pass


class SomeWrongImplementationC(C):
    def my_abstract_method(self):
        pass


class SomeCorrectImplementationC(C):
    def my_abstract_method(self):
        pass

    @classmethod
    def my_abstract_classmethod(cls):
        pass


SomeCorrectImplementationC()
SomeWrongImplementationC()
