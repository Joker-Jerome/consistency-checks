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
    #eturn DBEngine.MYSQL
    return DBEngine.POSTGRES


def db_config() -> dict:
    return {
        'user': 'postgres',
        'password': 'postgres',
        'database': 'omop',
        'host': '45.79.170.93',
        'port': 8099
    }


def slack_token() -> str:
    """
    When not None, then this slack webhook is notified of failed consistency checks.
    Slack channel's token (i.e. EXAMPLE/SLACK/TOKEN) can be retrieved from the
    channel's app "Incoming WebHooks" configuration as part of the Webhook URL.
    Idea taken from Mara framework: https://github.com/mara
    """
    return None
