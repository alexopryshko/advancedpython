from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('../ctypes/lib1.so')

ffi.cdef('''
int sum(int* arr, int len);
''')

arr = [1, 2, 3, 4, 5]
c_arr = ffi.new('int[]', arr)

s = lib.sum(c_arr, len(arr))
print(s)



