class B:
    def __le__(self, other):
        print('__le__')
        return False
    def __eq__(self, other):
        print('__eq__', self, other)
        return NotImplemented
    def __ne__(self, other):
        print('__ne__', self, other)
        return True
    def __ge__(self, other):
        print('__ge__')
        return NotImplemented


a = B()
b = B()
print(a == b)
# print(a >= b)
