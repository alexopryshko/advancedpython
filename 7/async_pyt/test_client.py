import aiohttp
from aioresponses import aioresponses


async def get_example():
    session = aiohttp.ClientSession()
    resp = await session.get('http://example.com')
    return await resp.text()


async def test_success():
    with aioresponses() as m:
        m.get('http://example.com', body='res1')
        m.get('http://example.com', body='res2')

        res1 = await get_example()
        res2 = await get_example()

    assert res1 == 'res1'
    assert res2 == 'res2'
