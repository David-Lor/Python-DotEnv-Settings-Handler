
# # Native # #
import os

# # Installed # #
# noinspection PyPackageRequirements
import pytest
import pydantic

# # Project # #
from dotenv_settings_handler import BaseSettingsHandler


class TestBaseSettingsHandler:
    """Test for the BaseSettingsHandler class, setting the system env vars on os.environ.
    We suppose python_dotenv load and set the system env variables correctly.
    """
    _created_env_vars = list()

    def teardown_method(self):
        """Teardown after each test method must remove all the system env variables created during the test.
        """
        for var_name in self._created_env_vars:
            os.environ.pop(var_name)
        self._created_env_vars.clear()

    def _write_env(self, **kwargs):
        """Call this method whenever system env variables must be set. Pass variables as kwargs.
        """
        os.environ.update(kwargs)
        self._created_env_vars.extend(kwargs.keys())

    def test_required_settings(self):
        """Test the class with two required parameters.
        """
        self._write_env(foo="localhost", bar="8080")

        class MySettings(BaseSettingsHandler):
            foo: str
            bar: str

        settings = MySettings()

        assert settings.foo == "localhost"
        assert settings.bar == "8080"

    def test_required_settings_missing(self):
        """Test the class with two required parameters, one of which is not defined as env variable.
        """
        self._write_env(foo="asdfghjkl")

        class MySettings(BaseSettingsHandler):
            foo: str
            bar: str

        with pytest.raises(pydantic.ValidationError):
            MySettings()

    def test_optional_settings_partial(self):
        """Test the class with one required parameter, one optional (defaulted) parameter,
        which is not defined as env variable.
        """
        self._write_env(bar="22")

        class MySettings(BaseSettingsHandler):
            foo = "127.0.0.1"
            bar: str

        settings = MySettings()

        assert settings.foo == "127.0.0.1"
        assert settings.bar == "22"

    def test_required_settings_defining_types(self):
        """Test the class with three required parameters: str, int, float.
        Parameters with types different than str must be converted to their target data type.
        """
        self._write_env(foo="172.17.0.1", bar="6472", baz="123.456")

        class MySettings(BaseSettingsHandler):
            foo: str
            bar: int
            baz: float

        settings = MySettings()

        assert settings.foo == "172.17.0.1"
        assert settings.bar == 6472
        assert settings.baz == 123.456

    def test_optional_settings_undefined_types(self):
        """Test the class with two optional (default) parameters, one of which is default to an int.
        Having that parameter set as an env variable, it must be automatically converted to int.
        """
        self._write_env(foo="192.168.0.1", bar="8088")

        class MySettings(BaseSettingsHandler):
            foo = "127.0.0.1"
            bar = 22

        settings = MySettings()

        assert settings.foo == "192.168.0.1"
        assert settings.bar == 8088

    def test_optional_settings_full(self):
        """Test the class with two optional (default) parameters, none of which is set as an env variable.
        """
        class MySettings(BaseSettingsHandler):
            foo = "10.0.0.1"
            bar = 3306

        settings = MySettings()

        assert settings.foo == "10.0.0.1"
        assert settings.bar == 3306

    def test_inherited_pydantic_case_insensitive(self):
        """Test the class setting with the case_insensitive option from pydantic.BaseSettings,
        testing if the BaseSettingsHandler is correctly inheriting pydantic.BaseSettings.
        The case from env variables and class fields are different but must match.
        """
        self._write_env(my_FOO="0.0.0.0", MY_bar="5000", MY_Baz="baz")

        class MyCaseSensitiveSettings(BaseSettingsHandler):
            my_foo: str
            my_bar: str
            my_baz: str

        with pytest.raises(pydantic.ValidationError):
            MyCaseSensitiveSettings()

        class MyCaseInsensitiveSettings(MyCaseSensitiveSettings):
            class Config:
                case_insensitive = True

        settings = MyCaseInsensitiveSettings()

        assert settings.my_foo == "0.0.0.0"
        assert settings.my_bar == "5000"
        assert settings.my_baz == "baz"

    def test_inherited_pydantic_prefixed(self):
        """Test the class setting with the env_prefix option from pydantic.BaseSettings,
        testing if the BaseSettingsHandler is correctly inheriting pydantic.BaseSettings.
        The field names set in the class are read as the env_prefix + the field name, all uppercase.
        """
        self._write_env(TESTAPP_FOO="192.168.0.0", TESTAPP_BAR="254")

        class MySettings(BaseSettingsHandler):
            foo: str
            bar: str

            class Config:
                env_prefix = "TESTAPP_"

        settings = MySettings()

        assert settings.foo == "192.168.0.0"
        assert settings.bar == "254"
