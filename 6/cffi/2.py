from cffi import FFI

ffi = FFI()

lib = ffi.dlopen('./lib2.so')

ffi.cdef('''
struct Point {
    int x;
    int y;
};
int area(struct Point *p1, struct Point *p2);
''')

p1 = ffi.new('struct Point*')
p2 = ffi.new('struct Point*')

p1.x = 0
p1.y = 0

p2.x = 10
p2.y = 10

s = lib.area(p1, p2)
print(s)


