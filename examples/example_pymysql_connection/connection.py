"""This example is based on creating a connection to a MySQL database using pymysql,
while the connection settings get loaded from a custom Settings class.
"""

# noinspection PyUnresolvedReferences,PyPackageRequirements
import pymysql
# noinspection PyUnresolvedReferences,PyPackageRequirements
from settings import my_settings as settings

connection = pymysql.connect(
    host=settings.DATABASE_SERVER,
    port=settings.DATABASE_PORT,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PORT,
    db=settings.DATABASE_DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
