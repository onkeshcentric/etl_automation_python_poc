from etlhelper import DbParams
import pathlib

path = pathlib.Path(__file__).parent.absolute()

SQLITEDB_SOURCE_PATH = str(path)+'\source.db'
SQLITEDB_DESTINATION_PATH = str(path)+'\destination.db'

SQLITEDB_SOURCE = DbParams(dbtype='SQLITE', filename=SQLITEDB_SOURCE_PATH)
SQLITEDB_DESTINATION = DbParams(dbtype='SQLITE', filename=SQLITEDB_DESTINATION_PATH)

#-----------------------------------------Dummy methods for DB Connection----------------------------------------------------#

# sqlalchemy#