class A:
    def __add__(self, other):
        print('__add__')

    def __iadd__(self, other):
        print('__iadd__')

    def __radd__(self, other):
        print('__radd__')

    def __neg__(self):
        print('__neg__')

    def __pos__(self):
        print('__pos__')

    def __invert__(self):
        print('__invert__')

    def __int__(self):
        print('__int__')
        return 1

class B:
    pass


a = A()
b = A()

a + b
a += b

a = A()
b = B()

a + b 
b + a

+a
-a
~a
int(a)