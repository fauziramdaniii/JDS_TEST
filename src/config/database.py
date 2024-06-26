
# src/config/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:P%40ssw0rd@localhost/jds_backend"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency untuk mengakses session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def get_engine():
#     return create_engine(SQLALCHEMY_DATABASE_URL)

