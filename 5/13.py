import asyncio
import random


async def gen_numbers(q: asyncio.Queue, *, count: int = 20):
    for num in range(count):
        await q.put(num)


async def process_numbers(q: asyncio.Queue, id: int):
    while True:
        num = await q.get()
        
        s = random.randint(0, 5)
        await asyncio.sleep(s)
        print(f'[{id}] Processed num={num}. slept {s}s')

        q.task_done()


async def main():
    random.seed(444)

    q = asyncio.Queue()
    coros = [
        gen_numbers(q, count=20),
        process_numbers(q, id=1),
        process_numbers(q, id=2),
        process_numbers(q, id=3),
    ]
    await asyncio.gather(*coros)


if __name__ == "__main__":
    asyncio.run(main())