# https://github.com/python/cpython/blob/bb86bf4c4eaa30b1f5192dab9f389ce0bb61114d/Objects/descrobject.c

# 1 property


class C:
    def getx(self): return self._x

    def setx(self, value): self._x = value

    def delx(self): del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")


class Property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)


class CWithDescriptor:
    def getx(self): return self._x

    def setx(self, value): self._x = value

    def delx(self): del self._x

    x = Property(getx, setx, delx, "I'm the 'x' property.")


c = C()
c1 = CWithDescriptor()
c.x = 1
c1.x = 1
print('c.__dict__', c.__dict__)
print('c1.__dict__', c1.__dict__)


# 2 static function
class E:
    def f(x):
        print(x)

    f = staticmethod(f)


class StaticMethod(object):
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f


# 3 class method
class ClassMethod(object):
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)

        def newfunc(*args):
            return self.f(klass, *args)

        return newfunc
