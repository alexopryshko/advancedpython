# 1


class A:
    def __getattr__(self, attr):
        print('__getattr__')

    field = 'field'


a = A()
a.name = 'name'

print('a.name', a.name)
print('a.field', a.field)
print('a.random', a.random)


# 2

class A:
    def __getattribute__(self, item):
        print('__getattribute__')

    def __len__(self):
        return 0

    def test(self):
        print('test', self)

    field = 'field'


a = A()
a.name = 'name'

print('a.name', a.name)
print('a.field', a.field)
print('a.random', a.random)
print('a.__len__', a.__len__)
print('len(a)', len(a))
print('type(a)...', type(a).__dict__['test'](a))
print('A.field', A.field)


# 3

class A:
    def __setattr__(self, key, value):
        print('__setattr__')

    field = 'field'


a = A()
a.field = 1
a.a = 1
print('a.__dict__', a.__dict__)
A.field = 'new'
print('A.field', A.field)


# 4

class A:
    def __getattribute__(self, item):
        if 'test' in item or '__dict__' == item:
            return super().__getattribute__(item)
        else:
            raise AttributeError


a = A()
a.test_name = 1
a.name = 1
print('a.__dict__', a.__dict__)
print('a.test_name', a.test_name)
print('a.name', a.name)
