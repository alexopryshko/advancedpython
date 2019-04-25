def select_all_from_test(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test;")
    res = cursor.fetchall()
    return [item[0] for item in res]
