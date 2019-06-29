import os
from dotenv_settings_handler import BaseSettingsHandler
from dotenv import load_dotenv

load_dotenv()


class MySettings(BaseSettingsHandler):
    DATABASE_SERVER = "127.0.0.1"
    DATABASE_PORT = 3306
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_DB: str


my_settings = MySettings()
