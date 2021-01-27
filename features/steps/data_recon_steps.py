from db.my_databases import REMOTE_MYSQL_SOURCE_DB,REMOTE_MYSQL_DESTINATION_DB
import sqlite3
from behave import *
from hamcrest import assert_that, equal_to


def find_count_table(conn, table_name):
    query = "select count(*) from " + table_name + ";"

    if(hasattr(conn, 'engine') and conn.engine.driver == 'pymysql'):
        return conn.execute(query).fetchone()
    else:
        cur = conn.cursor()
        count = cur.execute(query).fetchone()
        return count[0]

@then('I fetch count for "{tbl}" table from "{db}" database')
def step_impl(context, tbl, db):
    if(db == 'source'):
        conn = context.connection['source']
    else:
        conn = context.connection['destination']

    context.count[str(tbl)] = find_count_table(conn, tbl)

@then('I validate the count between tables "{table1}" and "{table2}"')
def step_impl(context, table1, table2):
    assert_that(context.count[table1] == (context.count[table2]), 'Values not equal: ' + str(context.count))
