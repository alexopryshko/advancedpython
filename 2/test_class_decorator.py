def slot(s):
    def _wrapper(clazz):
        class Wrapper(clazz):
            __slots__ = s

            def __init__(self, *args):
                assert len(args) == len(s)
                for k, v in zip(s, args):
                    setattr(self, k, v)

        return Wrapper
    return _wrapper


@slot(['a', 'b', 'c'])
class Test:
    pass


a = Test(1, 2, 3)
print(a.a, a.b, a.c)
b = Test(1)
