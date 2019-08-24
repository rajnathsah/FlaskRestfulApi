from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Index
from sqlalchemy import create_engine
import datetime
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash,check_password_hash

engine = create_engine("sqlite:///sample.db", echo=True)

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"

    employee_id = Column(Integer,index=True, primary_key=True)
    employee_name = Column(String, nullable=False)
    employee_sal = Column(Integer)

class Login(Base):
    __tablename__ = "login"

    username = Column(String, index=True, primary_key=True)
    password = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False, default=datetime.datetime.now())

Base.metadata.create_all(engine)

session = Session(engine)

employee = [
    Employee(employee_name='Tom', employee_sal=1000),
    Employee(employee_name='John', employee_sal=1500)
    ]

session.bulk_save_objects(employee)
session.commit()

login = Login(username="admin",password=generate_password_hash("admin@1234"))
session.add(login)
session.commit()

session.close()