import ctypes
from typing import List

lib1 = ctypes.CDLL('./lib1.so')
lib1.sum.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)


def sum(arr: List[int]) -> int:
    arr_len = len(arr)
    arr_type = ctypes.c_int * arr_len
    result = lib1.sum(100, arr_type(*arr), ctypes.c_int(arr_len))
    return int(result)


if __name__ == '__main__':
    print(sum([1, 2, 3, 4, 5]))
    print(sum([100, 101, 102, 103, 104, 105]))