import inspect


class B:
    def __le__(self, other):
        print('__le__')
        return False


print('getmembers', inspect.getmembers(B))


def foo(a, *, b:int, **kwargs):
    pass


print('getfile', inspect.getfile(foo))
print('getmodule', inspect.getmodule(foo))
print('getsource', inspect.getsource(foo))
print('signature', inspect.signature(foo))
print('')


def a(i):
    if i == 5:
        frame = inspect.currentframe()
        while frame.f_back:
            print(frame.f_code.co_name)
            frame = frame.f_back
        print(inspect.stack())
        return
    a(i + 1)


a(1)
