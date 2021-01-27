from behave import *
from hamcrest import assert_that, equal_to
import numpy as np

def distinct_count(conn, table_name, primary_column_name):
    query = "select count(DISTINCT "+primary_column_name+") from "+table_name+";"

    if (hasattr(conn, 'engine') and conn.engine.driver == 'pymysql'):
        return conn.execute(query).fetchone()
    else:
        cur = conn.cursor()
        count = cur.execute(query).fetchone()
        return count[0]

def column_data(conn, table_name, primary_column_name):
    query = "select "+primary_column_name+" from "+table_name+";"

    if (hasattr(conn, 'engine') and conn.engine.driver == 'pymysql'):
        result = conn.execute(query).fetchall()
        result = [r for r, in result]
        return result
    else:
        cur = conn.cursor()
        result = cur.execute(query).fetchall()
        result = [r[0] for r in result]
        return result

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

@then('I fetch all "{col_name}" in "{tbl}" table from "{db}" database')
def step_impl(context, col_name, tbl, db):
    if(db == 'source'):
        conn = context.connection['source']
    else:
        conn = context.connection['destination']

    context.column_data[str(tbl)] = column_data(conn, tbl, col_name)

@then('I validate the column data between tables "{table1}" and "{table2}"')
def step_impl(context, table1, table2):
    arr_1 = np.array(context.column_data[table1])
    arr_2 = np.array(context.column_data[table2])
    if context.remote:
        arr_2 = np.array([str(ele).replace('-', '') for ele in arr_2])
    else:
        arr_2 = np.array([str(ele).replace('-', '') for ele in arr_2]).astype(np.int)

    result = np.array_equal(arr_1,arr_2)
    print(result)
    assert_that(result, equal_to(True), 'Values not equal')