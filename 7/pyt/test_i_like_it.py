import pytest


@pytest.fixture()
def f():
    print(1)


@pytest.mark.usefixtures('f')
def test_success():
    assert True


@pytest.mark.parametrize('a,b,res', [
    (5, 2, 2.5),
    (0, 2, 0),
    (4, 2, 2),
    (-4, 2, -2)
])
def test_div(a, b, res):
    assert a / b == res
