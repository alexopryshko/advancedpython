from __future__ import print_function
try:
    import urllib.request as r
except ImportError:
    import urllib as r

import time


def perform_request():
    response = r.urlopen('http://python.org/')
    html = response.read()
    print(len(html))


begin = time.time()
perform_request()
perform_request()
print(time.time() - begin)
