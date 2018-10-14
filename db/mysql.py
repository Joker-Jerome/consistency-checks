import pymysql
from contextlib import contextmanager


@contextmanager
def mysql_db_connection(cursor_factory=None):
    try:
        from config import db_config
        db = db_config()
        con = pymysql.connect(user=db['user'],
                              db=db['database'],
                              host=db['host'],
                              password=db['password'] if db['password'] is not None else '',
                              port=int(db['port']),
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
        if cursor_factory is not None:
            cur = con.cursor(cursor=cursor_factory)
        else:
            cur = con.cursor()
    except pymysql.Error as err:
        yield None, None, err
    else:
        try:
            yield con, cur, None
        finally:
            cur.close()
            con.close()


def execute_mysql_query(query: str) -> float:
    with mysql_db_connection() as (_, cursor, _):
        cursor.execute(query)
        result = cursor.fetchone()
        return float(list(result.values())[0])
