import socket
from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()

class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        print(f'[future/{id(self)}] set_result: {result}')
        self.result = result
        for fn in self._callbacks:
            fn(self)


class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        print('Task.__init__')
        self.step(f)

    def step(self, future):
        print(f'step fut={id(future)}; fut.result={future.result}')
        try:
            next_future = \
                self.coro.send(future.result)
        except StopIteration:
            return

        print('add cb to next_future=', id(next_future))
        next_future.add_done_callback(self.step)


class Fetcher:
    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass

        f = Future()

        def on_connected():
            print('[fetch] on_connected cb')
            f.set_result(None)

        selector.register(self.sock.fileno(),
                          EVENT_WRITE,
                          on_connected)

        print(f'[fetch] before yield. my fut={id(f)}')
        result = yield f
        print(f'[fetch] after yield. my fut={id(f)}, result={result}')
        selector.unregister(self.sock.fileno())
        print('connected!')


def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()

# Begin fetching http://xkcd.com/353/
fetcher = Fetcher()
Task(fetcher.fetch())
loop()