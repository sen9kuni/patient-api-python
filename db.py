from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:@localhost:3306/hospital_zicare'

ENGINE = create_engine(
    SQLALCHEMY_DATABASE_URL,
    encoding='utf-8',
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
