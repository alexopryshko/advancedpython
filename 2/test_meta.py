# 1

class AMeta(type):
    def __new__(mcs, name, bases, classdict, **kwargs):
        cls = super().__new__(mcs, name, bases, classdict)
        print('Meta __new__', cls)
        return cls

    def __init__(cls, name, bases, classdict, **kwargs):
        print('Meta __init__', cls)
        super().__init__(name, bases, classdict, **kwargs)

    def __call__(cls):
        print('Meta __call__')
        return super().__call__()

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print('Meta __prepare__', **kwargs)
        return {'b': 2, 'a': 2}


class A(metaclass=AMeta):
    a = 1

    def __new__(cls):
        self = super().__new__(cls)
        print('class __new__', self)
        return self

    def __init__(self):
        print('class __init__')

    def __call__(self):
        print('class __call__')
        pass


a = A()
print(a.a)
print(a.b)

Another = AMeta('Test', (), {}, kw1=1, kw2=2)