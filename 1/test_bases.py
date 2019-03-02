class A:
    pass


class B(A):
    pass


class C:
    pass


class D(B, C):
    pass


print(D.__base__)
print(D.__bases__)
print(D.__mro__)
