# Python-DotEnv-Settings-Handler

A Settings Handler to be used with [python-dotenv](https://github.com/theskumar/python-dotenv) to load and read all the settings from a Settings class.

Instead of loading the env variables as `os.getenv("MY_VAR")`, create a class with all your env variables, and load them as `settings.MY_VAR`.

## Requirements

- Python 3.x (tested on Python 3.7)
- Libraries: python-dotenv, pydantic

## Changelog

- 0.0.1 - Initial release

## Example

Start by creating a `.env` file, as you would usually do using python-dotenv, or define all or some of these variables as system environment variables.

```
DATABASE_PORT=33306
DATABASE_USER=foo
DATABASE_PASSWORD=bar
DATABASE_DB=mydb
```

Then, create a new class inheriting from SettingsHandler:
- SettingsHandler inherits from pydantic.BaseSettings, working in a similar manner as pydantic.BaseModel. Check [pydantic documentation](https://pydantic-docs.helpmanual.io/) to know more about it.
- Basically you must define on your custom class the wanted ENV variables, which must have the same name as on the .env file.
- You can define a default value to be used if a certain variable is not defined on the .env file (in the example: DATABASE_SERVER, DATABASE_PORT).
- You should set the data type (str, int) on the values without default value (in the example: DATABASE_USER, DATABASE_PASSWORD, DATABASE_DB).
- If an env variable without default value not exists, when creating an instance of MySettings() a pydantic exception will be raised, asking to fill a required class attribute.

```python
# settings.py

from dotenv_settings_handler import SettingsHandler

class MySettings(SettingsHandler):
    DATABASE_SERVER = "127.0.0.1"
    DATABASE_PORT = 3306
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_DB: str

my_settings = MySettings()
```

Finally, you can import the `my_settings` class instance anywhere you want to use these settings:

```python
# connection.py

from .settings import my_settings as settings
import pymysql

connection = pymysql.connect(
    host=settings.DATABASE_SERVER,
    port=settings.DATABASE_PORT,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    db=settings.DATABASE_DB,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
```

This is what happened to each ENV var:

- DATABASE_SERVER: not defined on .env, so defaults to "127.0.0.1"
- DATABASE_PORT: defined on .env as 33306. Since in the class defaults to 3306 (an int), is automatically casted to int by pydantic.
- DATABASE_USER, DATABASE_PASSWORD, DATABASE_DB: defined on .env, and have no default values, so they are required. Not defining them on the .env file, nor as system env variables, would raise a pydantic exception when creating the MySettings() instance at settings.py.
