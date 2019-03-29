
import multiprocessing

import time

COUNT = 100000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    # spawn, forkserver
    multiprocessing.set_start_method('fork')
    begin = time.time()
    with multiprocessing.Pool(2) as p:
        p.apply_async(countdown, (COUNT,))
        p.apply_async(countdown, (COUNT,))
        p.close()
        p.join()
    print(time.time() - begin)
