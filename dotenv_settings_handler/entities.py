"""Definition of BaseSettingsHandler, the class inherited on the custom classes created to set settings env vars.
"""

# # Native # #
import os

# # Installed # #
import pydantic


class BaseSettingsHandler(pydantic.BaseSettings):

    class Config:
        env_prefix = ""  # Disable pydantic.BaseSettings ENV Prefix

    def __init__(self, **data):
        # Add env vars to **data
        for var_name in self.__fields__:
            var_value = os.getenv(var_name)
            if var_value is not None:
                data[var_name] = var_value

        super().__init__(**data)
