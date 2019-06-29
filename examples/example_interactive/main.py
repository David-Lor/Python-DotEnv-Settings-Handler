"""This example read the settings and print them out, so you can check how they get loaded.
"""

# noinspection PyUnresolvedReferences,PyPackageRequirements
from settings import my_settings as settings

print("Redis Host:", settings.redis_host)
print("Redis Port:", settings.redis_port)
print("Redis Port / 2:", settings.redis_port / 2)
print("API Port:", settings.api_port)
print("API Port * 2:", settings.api_port * 2)
print("API Password:", settings.api_password)
print("API Token:", settings.api_token)
