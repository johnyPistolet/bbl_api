from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+cymysql://r00t:our_sec_pass@localhost:3306/bbl_rest_api"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()