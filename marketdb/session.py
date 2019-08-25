from dotenv import load_dotenv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def get_session(env_path='.env'):
    load_dotenv(dotenv_path=env_path)
    sqltype = getenv("SQL_TYPE")
    port = getenv("DB_PORT")
    usr = getenv("DB_USER")
    host = getenv("DB_HOST")
    pwrd = getenv("DB_PASSWORD")
    name = getenv("DB_NAME")
    url = f'{sqltype}://{usr}:{pwrd}@{host}:{port}/{name}'
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    return Session

Base = declarative_base()
