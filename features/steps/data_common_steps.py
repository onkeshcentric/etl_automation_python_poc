from db.my_databases import SQLITEDB_SOURCE_PATH, SQLITEDB_DESTINATION_PATH, MYSQL_SOURCE, MYSQL_DESTINATION
import sqlite3
from behave import *


@given('I connect to source and destination databases')
def connect_to_db(context):
    context.connection['source'] = sqlite3.connect(SQLITEDB_SOURCE_PATH)
    context.connection['destination'] = sqlite3.connect(SQLITEDB_DESTINATION_PATH)

@given('I connect to the remote source and destination databases')
def connect_to_remote_db(context):
    context.connection['source'] = MYSQL_SOURCE.connect()
    context.connection['destination'] = MYSQL_DESTINATION.connect()
    context.remote = True