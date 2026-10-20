from operator import attrgetter

from configs import settings

(
    dialect,
    driver,
    username,
    password,
    host,
    port,
    database,
) = attrgetter(
    "db_provider",
    "db_driver",
    "db_user",
    "db_password",
    "db_host",
    "db_port",
    "db_name",
)(settings)
