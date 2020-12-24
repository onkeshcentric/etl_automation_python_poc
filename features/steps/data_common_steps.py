from db.my_databases import SQLITEDB_SOURCE_PATH, SQLITEDB_DESTINATION_PATH
import sqlite3
from behave import *


@given('I connect to source and destination databases')
def connect_to_db(context):
    context.connection['source'] = sqlite3.connect(SQLITEDB_SOURCE_PATH)
    context.connection['destination'] = sqlite3.connect(SQLITEDB_DESTINATION_PATH)

