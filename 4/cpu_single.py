import time

COUNT = 50000000


def countdown(n):
    while n > 0:
        n -= 1


begin = time.time()
countdown(COUNT)
countdown(COUNT)

print(time.time() - begin)
