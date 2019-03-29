from __future__ import print_function

from threading import Thread

try:
    import urllib.request as r
except ImportError:
    import urllib as r

import time


def perform_request():
    response = r.urlopen('http://python.org/')
    html = response.read()
    print(len(html))


t1 = Thread(target=perform_request, args=())
t2 = Thread(target=perform_request, args=())

begin = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print(time.time() - begin)
