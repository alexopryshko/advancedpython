import pytest


def test_upper():
    assert 'foo'.upper() == 'FOO'


def test_isupper():
    assert 'FOO'.isupper()
    assert not 'Foo'.isupper()


def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']

    try:
        s.split(1)
        assert False
    except TypeError:
        assert True


@pytest.fixture(scope='function', autouse=False)
def f():
    print(1)
    yield
    print(2)


def test_success(f):
    assert True
    # res = []

    # assert res is None
    # assert res is False
    # assert res == {}
    # assert res == []
    # assert isinstance(res, list)

