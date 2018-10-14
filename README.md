SQL Consistency checks
-------

Utility to run data consistency checks against a SQL database.

Project uses **Python 3.6** 

## Installation
1. Install `pip` and `virtualenv` ([how  to?](https://pip.pypa.io/en/stable/installing/))
2. Create virtualenv ``virtualenv .venv``
3. Enter to virtualenv ``source .venv/bin/activate``
4. Install required python libraries by run `pip install -r requirements.txt`
5. Configure DB connection on `config.py` file.
6. Run example consistency checks: `python example_consistency_checks.py`

## Usage
This utility provides a way of programmatically run consistency checks on a MySQL or PostgreSQL database and get notified.

A given consistency check accepts two input SQL queries that must return a numeric value (e.g. count, sum), and then the two resulting values are evaluated with the provided comparison operator (equal, not equal, smaller than or equal).

It also incorporates a module to notify of failing checks via Slack web hook.
