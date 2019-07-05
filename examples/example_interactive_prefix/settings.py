"""Create and initialize a single custom settings class.
"""

from typing import Optional
from dotenv_settings_handler import BaseSettingsHandler
from dotenv import load_dotenv

load_dotenv()


class MySettings(BaseSettingsHandler):
    class Config:
        env_prefix = "RANDOM_APP_"

    redis_host = "127.0.0.1"
    redis_port = 6379
    api_port = 5000
    api_password: str
    api_token: Optional[str]


my_settings = MySettings()
