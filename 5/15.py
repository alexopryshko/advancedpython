import asyncio
import random


async def connect_to_db(event: asyncio.Event, lock: asyncio.Lock):
    async with lock:
        print('Connecting...')
        await asyncio.sleep(3)
        print('Connected!')
        event.set()


async def gen_numbers(q: asyncio.Queue, *, count: int = 20):
    for num in range(count):
        await q.put(num)


async def process_numbers(q: asyncio.Queue,
                          event: asyncio.Event,
                          id: int):
    await event.wait()
    print(f'[{id}] Event is set!')

    while True:
        num = await q.get()
        
        s = random.randint(0, 5)
        await asyncio.sleep(s)
        print(f'[{id}] Processed num={num}. slept {s}s')

        q.task_done()


async def main():
    random.seed(444)

    q = asyncio.Queue()
    event = asyncio.Event()
    lock = asyncio.Lock()
    coros = [
        connect_to_db(event, lock),
        connect_to_db(event, lock),
        connect_to_db(event, lock),
        gen_numbers(q, count=20),
        process_numbers(q, event, id=1),
        process_numbers(q, event, id=2),
        process_numbers(q, event, id=3),
    ]
    await asyncio.gather(*coros)


if __name__ == "__main__":
    asyncio.run(main())