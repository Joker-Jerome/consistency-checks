from enum import Enum
from config import db_engine, DBEngine
from utils import send_slack_notification
from db.mysql import execute_mysql_query
from db.postgresql import execute_pg_query


class RelationType(Enum):
    EQUAL = 1
    NOT_EQUAL = 2
    SMALLER_THAN_OR_EQUAL = 3


def execute_query(query: str) -> float:
    if db_engine() == DBEngine.MYSQL:
        return execute_mysql_query(query)
    elif db_engine() == DBEngine.POSTGRES:
        return execute_pg_query(query)


def assert_relation(description: str, query_1: str, query_2: str, relation: RelationType):
    try:
        result_count_1 = execute_query(query_1)
        result_count_2 = execute_query(query_2)

        if relation == RelationType.EQUAL:
            assert result_count_1 == result_count_2
        elif relation == RelationType.NOT_EQUAL:
            assert result_count_1 != result_count_2
        elif relation == RelationType.SMALLER_THAN_OR_EQUAL:
            assert result_count_1 <= result_count_2
        else:
            print('Bad relation type!')
    except TypeError:
        err_msg = f'Assertion: "{description}" failed. Queries should return a single numeric value (e.g. count)'
        send_slack_notification(err_msg)
        print(err_msg)
    except AssertionError:
        err_msg = f"""Assertion "{description}" failed.
```        
Got {result_count_1}:
{query_1}
Expected {result_count_2}:
{query_2}
```
        """
        send_slack_notification(err_msg)
        print(err_msg)
    except Exception as e:
        err_msg = f'Error running Assertion "{description}". Error msg: ' + str(e)
        send_slack_notification(err_msg)
        print(err_msg)


def assert_equal(description: str, query_1: str, query_2: str):
    assert_relation(description, query_1, query_2, RelationType.EQUAL)


def assert_not_equal(description: str, query_1: str, query_2: str):
    assert_relation(description, query_1, query_2, RelationType.NOT_EQUAL)


def assert_smaller_than_or_equal(description: str, query_1: str, query_2: str):
    assert_relation(description, query_1, query_2, RelationType.SMALLER_THAN_OR_EQUAL)
