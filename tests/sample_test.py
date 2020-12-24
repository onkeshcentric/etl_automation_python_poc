from db.my_databases import SQLITEDB_SOURCE, SQLITEDB_DESTINATION, SQLITEDB_SOURCE_PATH, SQLITEDB_DESTINATION_PATH
from etlhelper import logger, get_rows,execute,executemany
import logging

logger.setLevel(logging.INFO)

def find_count_table(conn, table_name):
    cur = conn.cursor()
    count = cur.execute("select count(*) from "+table_name+";").fetchone()
    return count[0]

def select_all(conn, table_name):
    cur = conn.cursor()
    res = cur.execute("select * from "+table_name+";").fetchall()
    return res

def distinct_count(conn, table_name, primary_column_name):
    cur = conn.cursor()
    count = cur.execute("select count(DISTINCT "+primary_column_name+") from "+table_name+";").fetchone
    return count[0]

import sqlite3

conn_source = sqlite3.connect(SQLITEDB_SOURCE_PATH)
conn_dest = sqlite3.connect(SQLITEDB_DESTINATION_PATH)
d = distinct_count(conn_source, 'claims', 'ID')
e = distinct_count(conn_dest, 'reports', 'ID')

print(strt(d) +"," + str(e))


# conn_source = sqlite3.connect(SQLITEDB_SOURCE_PATH)
# conn_dest = sqlite3.connect(SQLITEDB_DESTINATION_PATH)
# d = find_count_table(conn_source, 'claims')
# e = find_count_table(conn_dest, 'reports')


# print(str(d)+","+str(e))


# res = select_all(conn_dest, 'reports')
#
# print(str(res))

# with SQLITEDB_SOURCE.connect() as conn1:
#     with SQLITEDB_DESTINATION.connect() as conn2:
#         sql_source = "SELECT * FROM claims"
#         sql_dest = "SELECT * FROM reports"
#
#         a = get_rows(sql_source, conn1)
#         b = get_rows(sql_dest, conn2)
#
#         print(str(a), str(b))
#
#         assert str(a) == str(b)
#

