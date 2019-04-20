from ctypes import *

class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]


point = POINT(10, 20)
print(point.x, point.y)

point = POINT(y=5)
print(point.x, point.y)

POINT(1, 2)


