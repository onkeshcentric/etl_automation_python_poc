from db.my_databases import SQLITEDB_SOURCE_PATH, SQLITEDB_DESTINATION_PATH
import sqlite3
from behave import *
from hamcrest import assert_that, equal_to


def distinct_count(conn, table_name, primary_column_name):
    cur = conn.cursor()
    count = cur.execute("select count(DISTINCT "+primary_column_name+") from "+table_name+";").fetchone()
    return count[0]

@then('I fetch distinct count for "{col_name}" in "{tbl}" table from "{db}" database')
def step_impl(context, col_name, tbl, db):
    if(db == 'source'):
        conn = context.connection['source']
    else:
        conn = context.connection['destination']

    context.count[str(tbl)] = distinct_count(conn, tbl, col_name)

@then('I validate the distinct count between tables "{table1}" and "{table2}"')
def step_impl(context, table1, table2):
    assert_that(context.count[table1] == (context.count[table2]), 'Values not equal: ' + str(context.count))