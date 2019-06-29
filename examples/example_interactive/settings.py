import os
from dotenv_settings_handler import BaseSettingsHandler
from typing import Optional


class MySettings(BaseSettingsHandler):
    redis_host = "127.0.0.1"
    redis_port = 6379
    api_port = 5000
    api_password: str
    api_token: Optional[str]


# Due to the examples structure, we must give the absolute path of the .env file
# However this should not be required in normal projects, and the .env file
# sould be placed at project/package root directory
dotenv_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), ".env")

my_settings = MySettings(dotenv_path=dotenv_file_path)
