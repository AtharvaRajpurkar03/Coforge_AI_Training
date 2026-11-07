import os # Activates virtual environments
from dotenv import load_dotenv # load_dotenv is a function
from sqlalchemy import create_engine 
# sqlalchemy is object relation model for DTOs: Data Transfer Object where we validate the models
# Its like Entity Framework CORE
from sqlalchemy.orm import sessionmaker, DeclarativeBase 
# Session Maker -> Use for creating sessions
# DeclarativeBase -> 
from sqlalchemy.engine import URL # URL is use for request

load_dotenv() # -> function

class Base(DeclarativeBase):
    pass

# Requests
database_url=URL.create( 
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT","3306")),
    database=os.getenv("DB_NAME","EmployeeDB")
)

engine=create_engine( # declaring url of database
    database_url
)

# sessionmaker in python -> perform database operations and add data in database
SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False # refreshes to insert new record
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
