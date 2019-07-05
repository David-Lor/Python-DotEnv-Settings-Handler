"""Create and initialize two settings classes (one for MySQL, one for MongoDB).
"""

from dotenv_settings_handler import BaseSettingsHandler
from dotenv import load_dotenv

load_dotenv()


class SQLSettings(BaseSettingsHandler):
    SQL_SERVER = "127.0.0.1"
    SQL_PORT = 3306
    SQL_USER: str
    SQL_PASSWORD: str
    SQL_DB: str


class MongoSettings(BaseSettingsHandler):
    MONGO_SERVER = "127.0.0.1"
    MONGO_PORT = 27017
    MONGO_DB: str


sql_settings = SQLSettings()
mongo_settings = MongoSettings()
