from django.db import connections
from django.db.utils import OperationalError


def check_database_connections(alias):
    db_conn = connections[alias]
    try:
        db_conn.cursor()
    except OperationalError:
        return False
    return True