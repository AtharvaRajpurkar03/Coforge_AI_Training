from sqlalchemy.orm import Session
from sqlalchemy import select,func
from models.bankcustomer_model import BankCustomer

def create_customer(db:Session,data):
    customer=BankCustomer(**data.model_dump())

    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_all_customers(db:Session,skip:int,limit:int):
    query=select(BankCustomer).offset(skip).limit(limit)
    result=db.scalars(query)
    return result.all()

def get_account(db:Session,account_number:str):
    query=select(BankCustomer).where(BankCustomer.account_number==account_number)
    result=db.scalar(query)
    return result

def update_customer(db:Session,account_number:str,data):
    customer=get_account(db,account_number)

    if not customer:
        return None

    customer.email=data.email
    customer.branch_name=data.branch_name

    db.commit()
    db.refresh(customer)
    return customer

def close_account(db:Session,account_number:str):
    customer=get_account(db,account_number)

    if not customer:
        return None

    if customer.balance>0:
        return "Balance exists"

    db.delete(customer)
    db.commit()
    return True

def filter_branch(db:Session,branch_name:str):
    query=select(BankCustomer).where(BankCustomer.branch_name==branch_name)
    result=db.scalars(query)
    return result.all()

def filter_account_type(db:Session,account_type:str):
    query=select(BankCustomer).where(BankCustomer.account_type==account_type)
    result=db.scalars(query)
    return result.all()

def deposit_amount(db:Session,account_number:str,amount):
    customer=get_account(db,account_number)

    if not customer:
        return None

    if not customer.is_active:
        return "Inactive"

    customer.balance+=amount

    db.commit()
    db.refresh(customer)
    return customer

def withdraw_amount(db:Session,account_number:str,amount):
    customer=get_account(db,account_number)

    if not customer:
        return None

    if not customer.is_active:
        return "Inactive"

    if amount>customer.balance:
        return "Insufficient"

    customer.balance-=amount

    db.commit()
    db.refresh(customer)
    return customer

def branch_deposits(db:Session):
    query = (select(BankCustomer.branch_name,func.sum(BankCustomer.balance).label("total_deposit")).group_by(BankCustomer.branch_name))
    result = db.execute(query)
    return result.all()
