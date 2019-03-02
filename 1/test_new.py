class A:
    _instance = None
    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


print(A())
print(A())

class A:
    def __new__(cls, *args):
        print('__new__')
        return None
    def __init__(self):
        print('__init__')

print(A())


