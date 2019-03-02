def cmp(a, b):
    print('a > b', a > b)
    print('a < b', a < b)
    print('a <= b', a <= b)
    print('a >= b', a >= b)
    print('a == b', a == b)
    print('a != b', a != b)


class A:
    def __lt__(self, other):
        print('__lt__')
    
    def __le__(self, other):
        print('__le__')
    
    def __eq__(self, other):
        print('__eq__')
    
    def __ne__(self, other):
        print('__ne__')
    
    def __gt__(self, other):
        print('__gt__')
    
    def __ge__(self, other):
        print('__ge__')


a = A()
b = A()
cmp(a, b)
print('')


class B:
    def __lt__(self, other):
        print('__lt__')
    def __le__(self, other):
        print('__le__')
        return NotImplemented
    def __eq__(self, other):
        print('__eq__', self, other)
        return NotImplemented
    def __ne__(self, other):
        print('__ne__', self, other)
        return False
    def __gt__(self, other):
        print('__gt__')
    def __ge__(self, other):
        print('__ge__')


a = B()
b = B()
cmp(a, b)