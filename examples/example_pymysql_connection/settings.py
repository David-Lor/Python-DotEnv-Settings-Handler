import os
from dotenv_settings_handler import BaseSettingsHandler


class MySettings(BaseSettingsHandler):
    DATABASE_SERVER = "127.0.0.1"
    DATABASE_PORT = 3306
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_DB: str


# Due to the examples structure, we must give the absolute path of the .env file
# However this should not be required in normal projects, and the .env file
# sould be placed at project/package root directory
dotenv_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), ".env")

my_settings = MySettings(dotenv_path=dotenv_file_path)
