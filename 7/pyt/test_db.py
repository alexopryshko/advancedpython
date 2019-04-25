import psycopg2
import pytest

from .db import select_all_from_test


@pytest.fixture(scope='session')
def conn():
    return psycopg2.connect(database="ap", user="alexander")


@pytest.fixture(autouse=True)
def rollback(conn):
    conn.rollback()


@pytest.fixture
def test1(conn):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO test VALUES ('1')""")


def test_success(test1, conn):
    res = select_all_from_test(conn)
    assert res == ['1']
