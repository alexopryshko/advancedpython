def test():
    a = []
    for i in range(5):
        def foo(b=i):
            print('i', i)
            print('b', b)

        print('__closure__ object', foo.__closure__)
        print('__closure__', [item.cell_contents for item in foo.__closure__])
        print('__defaults__ object', hex(id(foo.__defaults__)))
        print('__defaults__', foo.__defaults__)
        a.append(foo)

    return a


res = test()
print('run')
for func in res:
    func()

print('__closure__ object', res[0].__closure__, res[1].__closure__)
print('__closure__ is', res[0].__closure__ is res[1].__closure__)
print('__closure__[0] is', res[0].__closure__[0] is res[1].__closure__[0])
print('__defaults__ object', hex(id(res[0].__defaults__)),
      hex(id(res[1].__defaults__)))
print('__defaults__ is', res[0].__defaults__ is res[1].__defaults__)


def test():
    a = 1

    def foo():
        print(a)

    def bar():
        print(a)

    return foo, bar


f, b = test()
print(f.__closure__, b.__closure__)
