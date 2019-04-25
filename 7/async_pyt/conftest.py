import pytest
from aiohttp.test_utils import loop_context

from .api import create_app


@pytest.fixture(scope='session')
def loop():
    with loop_context() as _loop:
        yield _loop


@pytest.fixture(scope='session')
def event_loop(loop):
    yield loop


@pytest.fixture(scope='session')
def app():
    yield create_app()


@pytest.fixture
async def cli(aiohttp_client, app):
    client = await aiohttp_client(app)
    yield client
