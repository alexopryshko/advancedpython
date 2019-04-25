import datetime
import uuid

import mock
import pytest
from freezegun import freeze_time


async def return_uuid():
    return str(uuid.uuid4().hex)


async def return_date():
    return datetime.datetime.now()


async def test_uuid():
    with mock.patch('uuid.uuid4') as uuid4:
        uuid4.return_value = mock.Mock(hex='uuid')
        res = await return_uuid()
    assert res == 'uuid'


async def test_date1():
    with freeze_time(datetime.datetime(2017, 10, 3, 12)):
        assert await return_date() == datetime.datetime(2017, 10, 3, 12)


@pytest.fixture
async def freeze_t():
    now = datetime.datetime(2017, 10, 3, 12)
    _freeze_time = freeze_time(now)
    _freeze_time.start()
    yield now
    _freeze_time.stop()


async def test_date2(freeze_t):
    assert await return_date() == datetime.datetime(2017, 10, 3, 12)
