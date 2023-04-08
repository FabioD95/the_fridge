from typing import Generator
from sqlmodel import create_engine, Session, SQLModel

from configs.config import DB_CONFIG


# define postgres sqlalchemy engine connection
def get_engine() -> Generator:
    url = "postgresql://{user}:{passwd}@{host}:{port}/{db}".format(
        user=DB_CONFIG["db_user"],
        passwd=DB_CONFIG["db_password"],
        host=DB_CONFIG["db_host"],
        port=DB_CONFIG["db_port"],
        db=DB_CONFIG["db_name"],
    )
    # print(url)
    engine = create_engine(url, echo=True)
    return engine


def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session


def create_table() -> bool:
    engine = get_engine()
    try:
        SQLModel.metadata.create_all(engine)
        print('tabelle create!')
        return True
    except Exception as message:
        raise Exception(message)