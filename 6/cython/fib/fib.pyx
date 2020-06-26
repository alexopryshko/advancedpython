cdef int fib(int n):
    cdef:
        int a
        int b
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b

def pyfib(n):
    return fib(n)