from db.my_databases import SQLITEDB_SOURCE_PATH, SQLITEDB_DESTINATION_PATH
import sqlite3
from behave import *
from hamcrest import assert_that, equal_to

@given('I connect to source and destination databases')
def connect_to_db(context):
    context.connection['source'] = sqlite3.connect(SQLITEDB_SOURCE_PATH)
    context.connection['destination'] = sqlite3.connect(SQLITEDB_DESTINATION_PATH)

def find_count_table(conn, table_name):
    cur = conn.cursor()
    count = cur.execute("select count(*) from "+table_name+";").fetchone()
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