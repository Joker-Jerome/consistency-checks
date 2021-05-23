import psycopg2
from contextlib import contextmanager


@contextmanager
def pg_db_connection(cursor_factory=None):
    try:
        from config import db_config
        db = db_config()
        con = psycopg2.connect(user=db['user'],
                               database=db['database'],
                               host=db['host'],
                               port=int(db['port']),
                               password=db['password'] if db['password'] is not None else '')
        if cursor_factory is not None:
            cur = con.cursor(cursor_factory=cursor_factory)
        else:
            cur = con.cursor()
    except psycopg2.Error as err:
        yield None, None, err
    else:
        try:
            yield con, cur, None
        finally:
            cur.close()
            con.commit()
            con.close()


def execute_pg_query(query: str) -> float:
    with pg_db_connection() as (_, cursor, _):
        cursor.execute(query)
        result = cursor.fetchone()
        return float(result[0])

def execute_pg_query(query: str) -> float:
    _, cursor, _ = pg_db_connection()
    cursor.execute(query)
    result = cursor.fetchone()
    return float(result[0])