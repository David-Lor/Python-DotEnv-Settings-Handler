# Python-DotEnv-Settings-Handler

A Settings Handler using [python-dotenv](https://github.com/theskumar/python-dotenv) and/or system environment variables, to read all the settings from a Settings class based on [pydantic](https://github.com/samuelcolvin/pydantic/).

Instead of loading the environment variables (from now on 'env vars') as `os.getenv("MY_VAR")`, create a class with all your env variables, and load them as `settings.MY_VAR`.

The Class init will look for env variables used as settings for your project. These variables can be system env variables, or be specified on a .env file.

## Requirements

- Python 3.x (tested on Python 3.7)
- Libraries: pydantic (python-dotenv is not called from this library)

## Installing

From pip:
```bash
pip install -U dotenv-settings-handler
```

From Github:
```bash
git clone https://github.com/David-Lor/Python-DotEnv-Settings-Handler
cd Python-DotEnv-Settings-Handler
python setup.py install
```

Test:
```bash
pip install -r requirements.txt
python setup.py test
```

## Changelog

- 0.0.3 - Add Tests
- 0.0.2 - Removed calling to load_dotenv from the BaseSettingsHandler init, since it would look for the .env file in the wrong path. Manually calling load_dotenv from the target project context is now required.
- 0.0.1 - Initial release

## Examples

Start by creating a `.env` file, as you would usually do using python-dotenv, or define all or some of these variables as system environment variables.

```
DATABASE_PORT=33306
DATABASE_USER=foo
DATABASE_PASSWORD=bar
DATABASE_DB=mydb
```

Then, create a new class inheriting from BaseSettingsHandler:
- BaseSettingsHandler inherits from pydantic.BaseSettings, working in a similar manner as pydantic.BaseModel. Check [pydantic documentation](https://pydantic-docs.helpmanual.io/#settings) to know more about it. You should be able to extend your class with pydantic features (read more in the examples).
- Basically you must define on your custom class the wanted ENV variables as fields (class attributes), which must have the same name as on the .env file.
- You can define a default value to be used if a certain variable is not defined on the .env file (in the example: DATABASE_SERVER, DATABASE_PORT).
- You should set the data type (str, int) on the values without default value (in the example: DATABASE_USER, DATABASE_PASSWORD, DATABASE_DB). Values with a default value will use the type of that value.
- If an env variable without default value not exists, when creating an instance of MySettings() a pydantic exception will be raised, asking to fill a required class attribute.
- Calling load_dotenv() from your Python module is required if using .env file, in order to lookup for the .env file in your module directory context.

```python
# settings.py

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

### Ignore env case

Since BaseSettingsHandler inherits from [pydantic.BaseSettings](https://pydantic-docs.helpmanual.io/#settings), we can take advantage of the features of BaseSettings, such as ignoring the env case. 
This means we can have the env var names in our class as lowercase, and define them in our system as uppercase, lowercase or mixed lower/uppercase. They will still be detected by pydantic and the BaseSettingsHandler.

Just modify your custom Settings class with the modifiers featured by pydantic.BaseSettings (under a nested `class Config`):

```python
# settings.py

from dotenv_settings_handler import BaseSettingsHandler

class MySettings(BaseSettingsHandler):
    my_foo: str
    MY_BAR: int

    class Config:
        case_insensitive = True

settings = MySettings()
```

Now you can set your .env and/or system env variables with any case you want; i.e. `my_foo`, `MY_foo`, `MY_FOO`, `my_FOO`, `my_Foo` are all valid and will be accesible through `settings.my_foo`. 

### Set env prefix

Another cool feature from pydantic.BaseSettings is setting a prefix on your env variables. By default pydantic set this as `APP_`, but on BaseSettingsHandler this feature is disabled. However, you can enable it again setting the `env_prefix` option under `class Config`.

```python
# settings.py

from dotenv_settings_handler import BaseSettingsHandler

class MySettings(BaseSettingsHandler):
    foo: str
    bar: int

    class Config:
        env_prefix = "PYTHON_APP_"

settings = MySettings()
```

Now the field `foo` will be read from the env var `PYTHON_APP_FOO` (note that it will look for an uppercase env var), and `bar` from `PYTHON_APP_BAR`.
