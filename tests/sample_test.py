from db.my_databases import SQLITEDB_SOURCE, SQLITEDB_DESTINATION, SQLITEDB_SOURCE_PATH, SQLITEDB_DESTINATION_PATH
from etlhelper import logger, get_rows,execute,executemany
import logging

logger.setLevel(logging.INFO)


def find_count_table(conn, table_name):
    cur = conn.cursor()
    count = cur.execute("select count(*) from "+table_name+";").fetchone()
    return count[0]

import sqlite3

conn_source = sqlite3.connect(SQLITEDB_SOURCE_PATH)
conn_dest = sqlite3.connect(SQLITEDB_DESTINATION_PATH)
d = find_count_table(conn_source, 'claims')
e = find_count_table(conn_dest, 'reports')

assert d == e

# with SQLITEDB_SOURCE.connect() as conn1:
#     with SQLITEDB_DESTINATION.connect() as conn2:
#         sql_source = "SELECT COUNT(*) FROM claims"
#         sql_dest = "SELECT COUNT(*) FROM reports"
#
#         a = get_rows(sql_source, conn1)
#         b = get_rows(sql_dest, conn2)
#
#         print(str(a), str(b))
#
#         assert str(a) == str(b)

