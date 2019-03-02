import time


class A:
    def foo(self):
        pass


a = A()
begin = time.time()
for _ in range(10000000):
    a.foo()
print('class', time.time() - begin)

begin = time.time()
binding = a.foo
for _ in range(10000000):
    binding()
print('binding', time.time() - begin)
