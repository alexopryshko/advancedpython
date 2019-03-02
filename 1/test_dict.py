# 1 рассмотрим где хранятся атрибуты класса и атрибуты объекта


class A:
    a_class = 'a_class'

    def __init__(self):
        self.a = 'a'


class B(A):
    b_class = 'b_class'

    def __init__(self):
        self.b = 'b'
        super().__init__()


a = A()
b = B()

print('a.__dict__', a.__dict__)
print('A.__dict__', A.__dict__)
print('b.__dict__', b.__dict__)
print('B.__dict__', B.__dict__)

# 2 попробуем получить значения полей
print('b.a_class', b.a_class)
print('b.b', b.b)

# 3 попробуем изменить значения объекта
b1 = B()
b1.a = 1
b.a = 2
b.b_class = 1
print('b.__dict__', b.__dict__)
print('b1.__dict__', b1.__dict__)
print('A.__dict__', A.__dict__)

# 4 попробуем изменить значение класса
B.a_class = 'new_a_class'
print('b.a_class', b.a_class)
print('b1.a_class', b1.a_class)
print('a.a_class', a.a_class)
print('A.__dict__', A.__dict__)
print('B.__dict__', B.__dict__)

A.a_class = 'new_new_a_class'
print('b.a_class', b.a_class)
a1 = A()
print('a.a_class', a.a_class)
print('a1.a_class', a1.a_class)
print('A.__dict__', A.__dict__)
