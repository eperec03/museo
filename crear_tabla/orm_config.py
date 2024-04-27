from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

url_object= URL.create(
    drivername="mysql+mysqlconnector",
    username="root",
    password="changeme",
    host="localhost",
    database='museo')
engine = create_engine(url_object)
Session = sessionmaker(bind=engine)
session = Session()
Base=declarative_base()
