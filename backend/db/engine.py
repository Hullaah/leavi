from sqlalchemy import URL, create_engine

from configs import settings

from .config import database, dialect, driver, host, password, port, username

db_url = URL.create(f"{dialect}+{driver}", username, password, host, port, database)

engine = create_engine(
    db_url,
    echo=settings.debug,
    pool_pre_ping=True,
)
