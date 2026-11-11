from sqlalchemy import Column,Integer,String,Boolean,Numeric,Date
from config.database import Base

class BankCustomer(Base):
    __tablename__ = "BankCustomers"

    customer_id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True
    )

    customer_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    account_number = Column(
        String(50),
        unique=True,
        nullable=False
    )

    account_type = Column(
        String(20),
        nullable=False
    )

    branch_name = Column(
        String(100),
        nullable=False
    )

    balance = Column(
        Numeric(12,2),
        nullable=False
    )

    is_active = Column(
        Boolean,
        nullable=False
    )

    opened_on = Column(
        Date,
        nullable=False
    )