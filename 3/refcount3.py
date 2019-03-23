import gc
import sys
import ctypes
import weakref

gc.disable()

# We are using ctypes to access our unreachable objects by memory address.
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]

class A:
    def __init__(self, b):
        self.b = b

    def __del__(self):
        print('del a')

class B:
    def __init__(self, a):
        self.a = a
    
    def __del__(self):
        print('del b')


a = A(None)
b = B(None)
b.a = a
a.b = b

a_id = id(a)
b_id = id(b)

print('before del', PyObject.from_address(a_id).refcnt)
print('before del', PyObject.from_address(b_id).refcnt)

del a
del b

print('after del', PyObject.from_address(a_id).refcnt)
print('after del', PyObject.from_address(b_id).refcnt)

gc.collect()

print('after gc', PyObject.from_address(a_id).refcnt)
print('after gc', PyObject.from_address(b_id).refcnt)

