from sqlalchemy import(Column,Integer,String,Numeric)
from config.database import Base

class Employee(Base):
    __tablename__="Employees" # format of creating table

    employee_id=Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    employee_name=Column(
        String(100),
        nullable=False # require value
    )

    age= Column(
        Integer,
        nullable=False
    )

    email=Column(
        String(150),
        unique=True,
        nullable=False
    )

    department=Column(
        String,
        nullable=False
    )

    designation=Column(
        String,
        nullable=False
    )

    salary=Column(
        Numeric(12,2),
        nullable=False
    )

    city=Column(
        String(100),
        nullable=False
    )





