from etlhelper import DbParams
from sqlalchemy import create_engine
import pathlib

path = pathlib.Path(__file__).parent.absolute()

SQLITEDB_SOURCE_PATH = str(path)+'\source.db'
SQLITEDB_DESTINATION_PATH = str(path)+'\destination.db'

SQLITEDB_SOURCE = DbParams(dbtype='SQLITE', filename=SQLITEDB_SOURCE_PATH)
SQLITEDB_DESTINATION = DbParams(dbtype='SQLITE', filename=SQLITEDB_DESTINATION_PATH)

#-----------------------------------------Dummy methods for DB Connection----------------------------------------------------#

# sqlalchemy#
REMOTE_MYSQL_MACHINE= 'ccpocmysql.mysql.database.azure.com:3306'
REMOTE_USERNAME= 'etlpoc@ccpocmysql'
REMOTE_PASSWORD= 'pks@2021root'
REMOTE_MYSQL_SOURCE_DB = 'stateinsurance'
REMOTE_MYSQL_DESTINATION_DB= 'reports'

MYSQL_SOURCE=create_engine("mysql+pymysql://"+REMOTE_USERNAME+":"+REMOTE_PASSWORD+"@"+REMOTE_MYSQL_MACHINE+"/"+REMOTE_MYSQL_SOURCE_DB,echo = False)
MYSQL_DESTINATION=create_engine("mysql+pymysql://"+REMOTE_USERNAME+":"+REMOTE_PASSWORD+"@"+REMOTE_MYSQL_MACHINE+"/"+REMOTE_MYSQL_DESTINATION_DB,echo = False)
