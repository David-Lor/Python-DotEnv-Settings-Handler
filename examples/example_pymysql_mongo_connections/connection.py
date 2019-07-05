"""This example is based on creating a connection to a MySQL database using pymysql,
while the connections settings get loaded from a custom Settings class.
"""

import pymysql
import pymongo
from settings import sql_settings
from settings import mongo_settings

sql_connection = pymysql.connect(
    host=sql_settings.SQL_SERVER,
    port=sql_settings.SQL_PORT,
    user=sql_settings.SQL_USER,
    password=sql_settings.SQL_PORT,
    db=sql_settings.SQL_DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

mongo_connection = pymongo.MongoClient(
    host=mongo_settings.MONGO_SERVER,
    port=mongo_settings.MONGO_PORT
)
mongo_db = mongo_connection[mongo_settings.MONGO_DB]
