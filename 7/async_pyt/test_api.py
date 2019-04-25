async def test_without_name(cli):
    resp = await cli.get('/')
    document = await resp.text()
    assert document == 'Hello, Anonymous'


async def test_with_name(cli):
    resp = await cli.get('/name')
    document = await resp.text()
    assert document == 'Hello, name'
