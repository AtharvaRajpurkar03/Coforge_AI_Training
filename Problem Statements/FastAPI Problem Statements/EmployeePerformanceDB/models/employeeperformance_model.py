from sqlalchemy import (Column,Integer,String,Numeric,Float)
from config.database import Base

class EmployeePerformance(Base):
    __tablename__="EmployeePerformance"

    employee_id=Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True
    )

    employee_name=Column(
        String(100),
        nullable=False
    )

    department=Column(
        String(100),
        nullable=False
    )

    designation=Column(
        String(100),
        nullable=False
    )

    salary=Column(
        Numeric(10,2),
        nullable=False
    )

    performance_rating=Column(
        Float,
        nullable=False
    )

    projects_completed=Column(
        Integer,
        nullable=False
    )

    attendance_percentage=Column(
        Float,
        nullable=False
    )

    review_year=Column(
        Integer,
        nullable=False
    )