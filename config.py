"""
Configures the Consistency checks app
"""

from enum import Enum


class DBEngine(Enum):
    MYSQL = 1
    POSTGRES = 2


def db_engine() -> DBEngine:
    """
    Configures the DB engine to use for the consistency checks
    """
    return DBEngine.MYSQL


def db_config() -> dict:
    return {
        'user': 'foo',
        'password': 'bar',
        'database': 'mydb',
        'host': '127.0.0.1',
        'port': 3306
    }


def slack_token() -> str:
    """
    When not None, then this slack webhook is notified of failed consistency checks.
    Slack channel's token (i.e. EXAMPLE/SLACK/TOKEN) can be retrieved from the
    channel's app "Incoming WebHooks" configuration as part of the Webhook URL.
    Idea taken from Mara framework: https://github.com/mara
    """
    return None
