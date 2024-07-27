from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases

# SQL Lite
# SQLALCHEMY_DATABASE_URL = "sqlite:///./budget_todo.db"

# Localhost Mac
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:rootpassword@localhost:3306/budget_todo"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://myuser:myuser@127.0.0.1:3306/budget_todo"

# SQL in docker
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:rootpassword@mysql/budget_todo"

# databases query builder
# database = databases.Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def create_tables():
#     Base.metadata.create_all(bind=engine)