import unittest

import psycopg2

from .db import select_all_from_test

conn = None


def setUpModule():
    global conn
    conn = psycopg2.connect(database="ap", user="alexander")


def tearDownModule():
    conn.close()


class TestSelect(unittest.TestCase):
    def setUp(self):
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO test VALUES ('1')""")

    def tearDown(self):
        conn.rollback()

    def test_success(self):
        res = select_all_from_test(conn)
        self.assertEqual(res, ['1'])
