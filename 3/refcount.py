import sys

foo = []

print(sys.getrefcount(foo))

def bar(a):
    print(sys.getrefcount(foo))

def bar1(a):
    bar(a)

bar(foo)
# bar1(foo)
print(sys.getrefcount(foo))